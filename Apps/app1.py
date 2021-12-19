from flask import Flask, make_response, jsonify, abort, request, blueprints, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def hello():

    return "Hello"


if __name__ == '__main__':
    app.run(port=8080)
