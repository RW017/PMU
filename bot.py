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
            'model': 'gpt-3.5-turbo',
            'messages': data['messages']
        }
    )
    return jsonify(response.json())

@app.route('/bot.html')
def bot_page():
    return render_template('bot.html')

@app.route('/find.html')
def find_page():
    return render_template('find.html')

@app.route('/home.html')
def home_page():
    return render_template('home.html')

@app.route('/test.html')
def test_page():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
