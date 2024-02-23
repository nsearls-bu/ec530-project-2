'''User management data model and API paths'''
from flask import Blueprint

user_management_bp = Blueprint('user_management_bp', __name__)

@user_management_bp.route('/create_user',methods=['POST'])
def create_user(email, username, password, age, first_name, last_name):
    '''
    Create user with data model: {
    "username": "alice@example.com",
    "email": "alice@example.com",
    "password": "password",
    "first_name": "Alice",
    "last_name": "Jackson",
    "age": "24"
    }
    Returns 200 for user created with ID
    '''
@user_management_bp.route('/get_user',methods=['GET'])
def get_user(email, username, id):
    '''
    Search or get user via user uid, username, email
    Returns 200 and user if user found
    '''

@user_management_bp.route('/update_user',methods=['PUT'])
def update_user(email, username, password, age, first_name, last_name):
    '''
    Updates user data returns 200 if successfully updated
    '''
@user_management_bp.route('/delete_user',methods=['DELETE'])
def delete_user(email, username, password, age, first_name, last_name):
    '''
    Deletes a user and deactivates their account
    '''

# def basic_authentication(func):
#     '''
#     Wrapper for other endpoints that enables basic authentication
#     Determine if user is authenticated with basic http authentication and return 401 if not
#     '''
