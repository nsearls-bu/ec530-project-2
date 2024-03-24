'''User management data model and API paths and authentication'''
from uuid import uuid4, UUID
from flask import Blueprint, request
from modules.tables import Users
from session_factory import get_my_session
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
    age = request.args.get('age', type=int)
    first_name = request.args.get('first_name', type=str)
    last_name = request.args.get('last_name', type=str)

    try:
        session = get_my_session()
        user = Users(username=username, firstname=first_name,
                     lastname=last_name, email=email, age=age)
        session.add(user)
        session.commit()
        session.refresh(user)

        if user:
            return {"user_id": user.user_id}, 201
        return "Unable to create user", 422
    except Exception as e:
        return f'Error reading responses: {str(e)}', 500
    finally:
        session.close()


@user_management_bp.route('/get_user', methods=['GET'])
def get_user():
    '''
    Search or get user via user uid, username, email
    Returns 200 and user if user found
    '''

    try:
        email = request.args.get('email', type=UUID)
        username = request.args.get('username', type=str)
        user_id = request.args.get('user_id', type=str)
        session = get_my_session()

        if email or username:
            # Query by email or username if possible
            if email and username:
                # Query by both email and username
                query = session.query(Users).filter(
                    (Users.email == email) | (Users.username == username)).first()
            elif email:
                # Query by email
                query = session.query(Users).filter(
                    Users.email == email).first()
            else:
                # Query by username
                query = session.query(Users).filter(
                    Users.username == username).first()
            if query == None:
                return 'User not found', 404
            return query.as_dict(), 200  # Assign the query result to res
        elif user_id:
            # Query by uid
            query = session.query(Users).filter(
                Users.user_id == user_id).first()
            if query == None:
                return 'User not found', 404
            return query.as_dict(), 200
        else:
            return 'Bad request', 400
    except Exception as e:
        return f'Error reading responses: {str(e)}', 500
    finally:
        session.close()


@user_management_bp.route('/update_user', methods=['PUT'])
def update_user():
    '''
    Updates user data returns 201 if successfully updated
    '''
    user_id = request.args.get('user_id', type=str)
    email = request.args.get('email', type=str)
    username = request.args.get('username', type=str)
    age = request.args.get('age', type=int)
    first_name = request.args.get('first_name', type=str)
    last_name = request.args.get('last_name', type=str)

    try:
        session = get_my_session()
        user = session.query(Users).filter_by(user_id=user_id).first()
        if not user:
            return 'User not found', 404

        user.email = email
        user.username = username
        user.age = age
        user.firstname = first_name
        user.lastname = last_name

        session.commit()
        return 'User updated successfully', 200
    except Exception as e:
        session.rollback()
        return f'Error updating user: {str(e)}', 500
    finally:
        session.close()


@user_management_bp.route('/delete_user', methods=['DELETE'])
def delete_user():
    '''
    Deletes a user and deactivates their account
    '''
    user_id = request.args.get('user_id', type=str)

    if not user_id:
        return 'User ID is required', 400

    session = get_my_session()

    try:
        user = session.query(Users).filter_by(user_id=user_id).first()
        if not user:
            return 'User not found', 404

        session.delete(user)
        session.commit()
        return 'User deleted successfully', 200
    except Exception as e:
        session.rollback()
        return f'Error deleting user: {str(e)}', 500
    finally:
        session.close()
