from flask import Flask, make_response, jsonify, abort, request, blueprints, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

if __name__ == '__main__':
    app.run(port=8000)
