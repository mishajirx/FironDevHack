from flask import Flask, make_response, jsonify, abort, request, blueprints
from waitress import serve

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
x = 0


@app.route('/')
def hello():
    return 'Hello world'


def main():
    serve(app)


if __name__ == '__main__':
    main()
