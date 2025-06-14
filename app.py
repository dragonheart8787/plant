from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
import requests

# 載入 API 金鑰
load_dotenv()
app = Flask(__name__, static_folder='static')
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/api/suggest", methods=["POST"])
def suggest():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    # 呼叫 Gemini API
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_KEY}"
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    response = requests.post(url, json=payload)
    result = response.json()
    
    try:
        text = result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        text = f"[錯誤] {e}\n{result}"

    return jsonify({"result": text})

if __name__ == "__main__":
    app.run(debug=True)
