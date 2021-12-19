from flask import Flask, make_response, jsonify, abort, request, blueprints, render_template, redirect
from flask_wtf import FlaskForm
from waitress import serve
from json import loads, dumps,load
from requests import get
import psycopg2
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

sites = load(open("sites.json"))
ans = {
    200: "Active",
    201: "Active",
    404: "Not found (404)",
    502: "Bad request",
    500: "Internal Server Error"
}


class LoginForm(FlaskForm):
    address = StringField('Полный адрес сайта', validators=[DataRequired()])
    submit = SubmitField('Добавить')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = LoginForm()
    if form.validate_on_submit():
        sites['sites'].append({"address": form.address.data, "state": "-"})
        print(sites)
        with open("sites.json", "w") as f:
            f.write(dumps(sites))
        return redirect('/')
    return render_template('newsite.html', title='Добавление IP', form=form)


@app.route('/')
def hello():
    for i in range(len(sites['sites'])):
        address = sites['sites'][i]['address']
        try:
            res = get(address)
            sites['sites'][i]['state'] = ans[res.status_code]
        except Exception:
            sites['sites'][i]['state'] = "Nonactive"
    return render_template('main.html', sites=sites)


def main():
    serve(app)


if __name__ == '__main__':
    main()
