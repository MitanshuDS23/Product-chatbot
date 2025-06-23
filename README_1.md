# Smart E-Commerce Chatbot Backend (Flask + MariaDB + Gemini AI)

This repository contains the backend code for a chatbot-powered e-commerce platform. The backend is built using Python's Flask framework, MariaDB for data storage, and integrates with Google Gemini AI to provide intelligent responses and product highlights.

## Features

- Search for products from a live database
- Chat interface with AI-generated product descriptions
- Google Gemini integration to enhance user interaction
- Command-based reseeding to reset and populate sample product data
- Modular architecture using Flask, SQLAlchemy, and REST APIs
- Logging of user queries and responses for session tracking

## Project Structure

```
/project-root
│
├── app.py                # Main Flask application with API routes
├── models.py             # Database models and search logic
├── chat_logger.py        # Logs chat sessions to a file or database
├── /venv                 # Python virtual environment
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chatbot-backend.git
cd chatbot-backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Activate the environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install flask flask-cors flask-sqlalchemy pymysql google-generativeai
```

### 4. Set up MariaDB

- Ensure your MariaDB server is running.
- Update the database connection string in `models.py` with your credentials.
- The application will automatically create and seed the product table on first run.

## Running the Application

Start the backend server:

```bash
python app.py
```

By default, the backend runs on: `http://localhost:9000`

## Using the Chatbot

Connect your frontend to the backend endpoint `/chat`. You can send messages like:

- "Search headphones"
- "Find mobile"
- "Reset products" (to reload 100 test items)

The system will return relevant products from the database along with a short AI-generated highlight for each product.

## Requirements

- Python 3.8 or above
- MariaDB installed and running locally or remotely
- Internet access to connect with Google Gemini API
- A valid Gemini API key configured in `app.py`

## License

This project is open-source and available under the MIT License.

## Author

Developed by [Your Name] — Contributions are welcome.

for frontend:

1. npm install
2. npm start
