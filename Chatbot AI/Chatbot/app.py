from flask import Flask, render_template, request
from chatbot import chatbot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['user_query']
    response = chatbot(user_query)
    return render_template('index.html', user_query=user_query, response=response)

if __name__ == '__main__':
    app.run(debug=True)
