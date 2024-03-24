from flask import Flask
from modules.user_management import user_management_bp
from modules.output import output_bp
from modules.document_uploader import document_db
from modules.nlp_analyser import analyser_bp




if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(user_management_bp)
    app.register_blueprint(output_bp)
    app.register_blueprint(document_db)
    app.register_blueprint(analyser_bp)
    