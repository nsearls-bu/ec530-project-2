'''User management data model and API paths and authentication'''
from uuid import uuid4, UUID
from flask import Blueprint, request

user_management_bp = Blueprint('user_management_bp', __name__)


@user_management_bp.route('/create_user', methods=['POST'])
def create_user():
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
    email = request.args.get('email', type=str)
    username = request.args.get('username', type=str)
    password = request.args.get('password', type=str)
    age = request.args.get('age', type=int)
    first_name = request.args.get('first_name', type=str)
    last_name = request.args.get('last_name', type=str)
    user_uid = uuid4()

    res = 'WRITE DATA TO DB'

    if res is not None:
        return res, 201
    return res, 400


@user_management_bp.route('/get_user', methods=['GET'])
def get_user(email, username, id):
    '''
    Search or get user via user uid, username, email
    Returns 200 and user if user found
    '''
    email = request.args.get(email, type=str)
    username = request.args.get('username', type=str)
    uid = request.args.get('uid', type=str)

    if email != None | username != None:
        # Query by email or username if possible
        res = 'some response'
    if uid != None:
        # Query by uid
        res = 'Some query response'
    if email is None and username is None and uid is None:
        return 400
    return res, 200


@user_management_bp.route('/update_user', methods=['PUT'])
def update_user(email, username, password, age, first_name, last_name):
    '''
    Updates user data returns 201 if successfully updated
    '''
    email = request.args.get('email', type=str)
    username = request.args.get('username', type=str)
    password = request.args.get('password', type=str)
    age = request.args.get('age', type=int)
    first_name = request.args.get('first_name', type=str)
    last_name = request.args.get('last_name', type=str)

    res = 'return from db'
    if res is not None:
        return res, 201
    return 400


@user_management_bp.route('/delete_user', methods=['DELETE'])
def delete_user():
    '''
    Deletes a user and deactivates their account
    '''

    uid = request.args.get('uid', type=UUID)

    res = 'Do something to db - delete user'
    if res is not None:
        return res, 204
    else:
        return 'Resource not found', 404

# def basic_authentication(func):
#     '''
#     Wrapper for other endpoints that enables basic authentication
#     Determine if user is authenticated with basic http authentication and return 401 if not
#     '''
