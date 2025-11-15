from flask import Flask, request, jsonify
import sqlite3
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests (so frontend JS can talk to backend)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Database setup
DB_NAME = "feedback.db"

def init_db():
    """Create feedback table if it doesn't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/feedback', methods=['POST'])
def add_feedback():
    """Add a new feedback entry"""
    data = request.get_json()
    name = data.get("name")
    message = data.get("message")

    if not name or not message:
        return jsonify({"error": "Name and message are required"}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

    logging.info(f"New feedback added: {name} - {message}")
    return jsonify({"status": "success", "message": "Feedback added successfully"}), 201


@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Fetch all feedback"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    rows = cursor.fetchall()
    conn.close()

    feedback_list = [{"id": row[0], "name": row[1], "message": row[2]} for row in rows]
    return jsonify(feedback_list), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Basic health check endpoint"""
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
