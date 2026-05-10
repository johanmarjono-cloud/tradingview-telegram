from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8796933153:AAEbw-3vSN-dVhu7RiySLtfljGagde8GhRA"
CHAT_ID = "-1003719740978"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    message = data.get("message", "NO SIGNAL")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, json=payload)

    return {"status": "success"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
