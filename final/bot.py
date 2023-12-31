from flask import Flask, request, jsonify, render_template
import requests
import openai

app = Flask(__name__)
openai.api_key = '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'
ENDPOINT = 'https://api.openai.com/v1/chat/completions'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}'
    }
    response = requests.post(
        ENDPOINT,
        headers=headers,
        json={
            'model': 'ft:gpt-3.5-turbo-0613:pmu:recipe-ner:8AqJpClH',
            'messages': data['messages']
        }
    )
    return jsonify(response.json())

@app.route('/bot.html')
def bot():
    return render_template("bot.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)