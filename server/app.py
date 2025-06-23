# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

from models import init_db, reset_and_seed, search_products
from chat_logger import log_chat

app = Flask(__name__)
CORS(app)

init_db(app)

genai.configure(api_key="AIzaSyBpPqMICSwAotfoziIK2W2aRJxfahyCYcs")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    if user_message.lower() in ("rese​ed products", "reset products"):
        log_chat(session_id, user_message, "Reseeding database...")
        with app.app_context():
            reset_and_seed()
        reply = "✅ Products table wiped and reseeded with 100 mock items."
        return jsonify({"response": reply})

    products = search_products(user_message)
    if products:
        enriched = []
        for name in products:
            ai_desc = model.generate_content(
                f"Give a short promotional line for this product: '{name}'"
            ).text
            cleaned = ai_desc.replace("*", "").strip()
            enriched.append(f"🛍️ {name} — {cleaned}")
        bot_reply = "\n\n".join(enriched)
    else:
        bot_reply = "❌ Sorry, no matching products found in our catalog."

    log_chat(session_id, user_message, bot_reply)
    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=9000)
