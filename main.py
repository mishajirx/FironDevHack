from flask import Flask, make_response, jsonify, abort, request, blueprints, render_template
from waitress import serve

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def hello():
    return render_template('base.html')


def main():
    serve(app)


if __name__ == '__main__':
    main()
