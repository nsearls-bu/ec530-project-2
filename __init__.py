from flask import Flask
from user_management import user_management_bp

app = Flask(__name__)
app.register_blueprint(user_management_bp)
