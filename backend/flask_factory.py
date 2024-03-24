'''Generates a flask application and creates a connection engine for sql'''
import os
from flask import Flask
from flask_cors import CORS
from modules.user_management import user_management_bp
from modules.output import output_bp
from modules.document_uploader import document_db
from modules.nlp_analyser import analyser_bp



def create_flask_app():
    '''Create flask app - register blueprint and set CORS for development'''
    flask_app = Flask(__name__)
    flask_app.register_blueprint(user_management_bp)
    flask_app.register_blueprint(output_bp)
    flask_app.register_blueprint(document_db)
    flask_app.register_blueprint(analyser_bp)
    CORS(flask_app)
    flask_app.config['CORS_HEADERS'] = 'Content-Type'
    return flask_app