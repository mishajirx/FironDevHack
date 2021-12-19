from flask import Flask, make_response, jsonify, abort, request, blueprints, render_template
from waitress import serve
from json import load

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


sites = load(open("sites.json"))

@app.route('/')
def hello():
    return render_template('base.html', sites=sites)


def main():
    serve(app)


if __name__ == '__main__':
    main()
