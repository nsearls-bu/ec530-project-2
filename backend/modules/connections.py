'''Does basic NLP analysis of text input'''
from uuid import uuid4, UUID
from flask import Blueprint, request
from modules.tables import Connections, NLP_Response, Documents
from session_factory import get_my_session


connection_bp = Blueprint('connections_bp', __name__)

from session_factory import get_my_session

@connection_bp.route('/create_engine', methods=['PUT'])
def create_engine_connection():
    '''
    Connects to container managing NLP processing or website API
    {'connection_name' : name
    connection_url: url
    connection_type: website API or other NLP processor}
    writes to connection table in table
    '''

    connection_name = request.args.get('name', type=str)
    url = request.args.get('url_name', type=str)
    connection_uid = uuid4()

    session = get_my_session()

    new_connection = Connections(id=connection_uid, connection_name=connection_name, url=url)
    session.add(new_connection)
    session.commit()
    res = session.refresh(new_connection)
    session.close()

    if res is not None:
        return res, 200
    return res, 400


analyser_bp = Blueprint('analyser_bp', __name__)


@connection_bp.route('/remove_engine', methods=['PUT'])
def remote_engine_connection(name, url):
    '''
    Connects to container managing NLP processing or website API
    {'connection_name' : name
    connection_url: url
    connection_type: website API or other NLP processor}
    writes to connection table in table
    '''
    connection_uid = request.args.get('connection_uid', type=UUID)

    if not connection_uid:
        return 'Connection UID is required', 400

    try:
        # Attempt to delete the connection from the database
        session = get_my_session()  # Assuming you have the session created as shown in the previous example
        connection = session.query(Connections).filter_by(id=connection_uid).first()

        if connection:
            # Using SQLAlchemy query to delete the connection
            session.query(Connections).filter_by(id=connection_uid).delete()
            session.commit()
            session.close()
            return 'Old connection deleted successfully', 204
        else:
            return 'Connection not found', 404
    except Exception as e:
        return f'Error deleting connection: {str(e)}', 500

