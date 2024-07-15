from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']  = 'aaaaa aaaaa a'
    return app