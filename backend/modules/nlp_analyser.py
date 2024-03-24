'''Does basic NLP analysis of text input'''
from uuid import uuid4, UUID
from flask import Blueprint, request
from modules.tables import Connections, NLP_Response


analyser_bp = Blueprint('analyser_bp', __name__)

from session_factory import get_my_session

@analyser_bp.route('/create_engine', methods=['PUT'])
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


@analyser_bp.route('/remove_engine', methods=['PUT'])
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


@analyser_bp.route('/create_response', methods=['GET'])
def create_response():
    '''
    Creates summary text from AI based NLP program
    returns:
        {
            user_uid: uid,
            document_id : document_id
            title: title_summary()
            summary: generate_summary()
            sentiment: generate_sentiment()
            keyword: keyword_analysis()
            similar_articles: web_search()
        }
    writes to response table in db
    '''
    uid = request.args.get('uid', type=UUID)
    document_id = request.args.get('document_id', type=UUID)

    document_text = 'QUERY document db with document id'

    # Input text fetched from document table

    def generate_summary(document_text):
        '''Uses prompt like "generate a summary of the following text"'''
    def title_summary(document_text):
        '''Generate a single sentence summary'''
    def generate_sentiment(document_text):
        '''Uses prompt like "Assess the overall sentiment of the following text on a scale of 1-5 where 1 is most negative and 5 is most positive"'''
    def keyword_analysis(document_text):
        '''Uses prompt like "Generate 15 keywords from the following text with definitions as key-pairs in a json'''
    def proper_noun_analysis(document_text):
        '''Record every proper noun in this document and output a list of names,locations, institutions, and addresses'''
    def web_search():
        '''Crafts a google search based on a keywords, summary, and article title - returns web links'''

    # Perform analyses
    title = title_summary(document_text)
    summary = generate_summary(document_text)
    sentiment = generate_sentiment(document_text)
    keywords = keyword_analysis(document_text)
    similar_articles = web_search()

    # Write the response to the database
    try:
        session = get_my_session()
        response = NLP_Response(
            user_uid=uid,
            document_id=document_id,
            title=title,
            summary=summary,
            sentiment=sentiment,
            keywords=keywords,
            similar_articles=similar_articles
        )
        session.add(response)
        session.commit()
        return 'Response created successfully', 200
    except Exception as e:
        return f'Error creating response: {str(e)}', 500