'''API for reading responses and outputting data to users'''

from uuid import UUID
from flask import Blueprint, request
from flask_factory import get_session_engine

output_bp = Blueprint('output_bp', __name__)


@output_bp.route('/get_responses', methods=['GET'])
def read_responses():
    '''  returns:
     {
         user_uid: uid,
         document_id : document_id
         title: title_summary()
         summary: generate_summary()
         sentiment: generate_sentiment()
         keyword: keyword_analysis()
         similar_articles: web_search()
     }
      If user adds response key - returns specific response value'''
    user_id = request.args.get('user_id', type=UUID)
    document_id = request.args.get('document_id', type=UUID)

    res = 'QUERY_DB'
    if res is not None:
        return res, 200
    return None, 404


@output_bp.route('/get_paragraph', methods=['GET'])
def get_paragraph():
    '''  returns:
     Returns paragraph from document database depending on document id and paragraph id
      If user adds response key - returns specific response value

      '''

    document_id = request.args.get('document_id', type=UUID)
    paragraph_id = request.args.get('paragraph_id', type=UUID)

    res = 'QUERY_DB'
    if res is not None:
        return res, 200
    return res, 404
