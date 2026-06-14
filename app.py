print("APP STARTED")
from flask import Flask, render_template, request, jsonify
import sqlite3

from chatbot import get_response
import database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json['message']

    bot_response = get_response(user_message)

    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats(user_message, bot_response) VALUES (?,?)",
        (user_message, bot_response)
    )

    conn.commit()
    conn.close()

    return jsonify({
        'response': bot_response
    })


@app.route('/logs')
def logs():

    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chats")

    data = cursor.fetchall()

    conn.close()

    return render_template('logs.html', chats=data)


if __name__ == "__main__":
    app.run(debug=True)