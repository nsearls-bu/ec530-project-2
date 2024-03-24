'''Does basic NLP analysis of text input'''
from uuid import uuid4, UUID
from flask import Blueprint, request
from modules.tables import Connections, NLP_Response, Documents
from session_factory import get_my_session
from task_queue.bridge import rabbitmq_client, redis_client
from pika import BasicProperties
import uuid
import pickle
from pydantic import BaseModel


class PendingTask(BaseModel):
    task_id: str
class ResultTask(BaseModel):
    output: str

analyser_bp = Blueprint('analyser_bp', __name__)


@analyser_bp.route('/create_response', methods=['POST'])
async def create_response():
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
    user_id = request.args.get('user_id', type=UUID)
    document_id = request.args.get('document_id', type=UUID)
    try:
        with get_my_session() as session:
            document_text = session.query(Documents).filter_by(
                document_id=document_id).first()
    except Exception as e:
        return f'Error reading responses: {str(e)}', 500
    if document_text is None:
        return "Document not found", 404
    # Input text fetched from document table

    def generate_summary(document_text):
        task_id = str(uuid.uuid4())

        rabbitmq_client.basic_publish(
            exchange='',  # default exchange
            routing_key='project2_queue',
            body=pickle.dumps(document_text),
            properties=BasicProperties(headers={'task_id': task_id})
        )

        return PendingTask(task_id=task_id)

    def title_summary(document_text):
        '''Generate a single sentence summary'''
        return None

    def generate_sentiment(document_text):
        '''Uses prompt like "Assess the overall sentiment of the following text on a scale of 1-5 where 1 is most negative and 5 is most positive"'''
        return None

    def keyword_analysis(document_text):
        '''Uses prompt like "Generate 15 keywords from the following text with definitions as key-pairs in a json'''
        return None

    def proper_noun_analysis(document_text):
        '''Record every proper noun in this document and output a list of names,locations, institutions, and addresses'''
        return None

    def web_search():
        '''Crafts a google search based on a keywords, summary, and article title - returns web links'''
        return None

    # Perform analyses
    # title = title_summary(document_text)
    # summary = generate_summary(document_text)
    # sentiment = generate_sentiment(document_text)
    # keywords = keyword_analysis(document_text)
    # similar_articles = web_search()
    summary_task = generate_summary(document_text.fulltext)

    title = None
    summary = None
    sentiment = None
    keywords = None
    similar_articles = None
    # We'll create some kind of poll to the worker and generate all of these tasks
    # Write the response to the database
    try:
        session = get_my_session()
        response = NLP_Response(
            user_id=user_id,
            document_id=document_id,
            title_summary=summary,
            sentiment_score=sentiment,
            keywords=keywords,
            similar_articles=similar_articles
        )
        session.add(response)
        session.commit()
        return {"summary_task": summary_task.model_dump(mode='json')}, 201
    except Exception as e:
        return f'Error creating response: {str(e)}', 500



@analyser_bp.route("/results/<task_id>")
async def nlp_results(task_id):
    '''Returns pending if not complete, or the result if done'''
    if not redis_client.exists(task_id):
        return PendingTask(task_id=task_id).model_dump()
    result = redis_client.get(task_id)
    return ResultTask(output=result).model_dump()