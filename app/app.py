# from flask import Flask, request
#
# app = Flask(__name__)
#
# @app.before_request
# def log_request_info():
#     app.logger.info('Headers: %s', request.headers)
#     app.logger.info('Body: %s', request.get_data())
#     app.logger.info('URL: %s', request.url)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return "It works"
#
# if __name__ == '__main__':
#     app.run(debug=True)

# your-project/app/app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello from AI-WAF", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
