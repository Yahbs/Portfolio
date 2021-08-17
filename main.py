from flask import Flask, render_template


portfolio = Flask(__name__)


@portfolio.route('/')
def index():
    return render_template('index.html')

