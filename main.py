from flask import Flask, make_response, jsonify, abort, request, blueprints, render_template
from waitress import serve
from json import load
from requests import get

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

sites = load(open("sites.json"))
ans = {
    200: "Active",
    201: "Active",
    404: "Not found (400)",
    502: "Bad request",
    500: "Internal Server Error"
}


@app.route('/')
def hello():
    for i in range(len(sites['sites'])):
        address = sites['sites'][i]['address']
        try:
            res = get(address)
            sites['sites'][i]['state'] = ans[res.status_code]
        except Exception:
            sites['sites'][i]['state'] = "Nonactive"
    return render_template('base.html', sites=sites)


def main():
    serve(app)


if __name__ == '__main__':
    main()
