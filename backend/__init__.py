'''Start the program here'''
from flask import Flask
from flask_factory import create_flask_app

if __name__ == '__main__':
    app = create_flask_app()
    app = Flask(__name__)

    app.run(port=4009)
    