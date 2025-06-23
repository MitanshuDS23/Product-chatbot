import json
import os
from datetime import datetime

LOG_FILE = "chat_logs.json"

def log_chat(session_id: str, user_msg: str, bot_response: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "user_message": user_msg,
        "bot_response": bot_response
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
