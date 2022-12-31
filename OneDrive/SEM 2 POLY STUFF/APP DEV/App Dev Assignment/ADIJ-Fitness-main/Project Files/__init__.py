from flask import Flask, redirect,render_template, session, flash
from route import route
from manageItem import get_item_list, list_cart

app = Flask(__name__)
app.register_blueprint(route)
app.secret_key = 'MyFlaskWebAppKey'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')


if __name__ == '__main__':
    app.run(debug=True)
