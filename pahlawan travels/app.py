from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 


TOKEN = "8523030030:AAHyREzKtZw_sw8jRvLVyMKxkfsUDU6ryog"
CHAT_ID = "1011962703"

@app.route('/send_booking', methods=['POST'])
def send_booking():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    tour = data.get('tour')

    
    text = (
        f"🚀 <b>Новая заявка!</b>\n\n"
        f"<b>Тур:</b> {tour}\n"
        f"<b>Имя:</b> {name}\n"
        f"<b>Телефон:</b> {phone}"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
    
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    
    app.run(port=5000, debug=True)