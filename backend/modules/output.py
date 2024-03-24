'''API for reading responses and outputting data to users'''

from uuid import UUID
from flask import Blueprint, request
from session_factory import get_my_session
from modules.tables import NLP_Response, Paragraphs

output_bp = Blueprint('output_bp', __name__)


@output_bp.route('/get_responses', methods=['GET'])
def read_responses():
    '''  returns:
     {
         user_id: uid,
         document_id : document_id
         title: title_summary()
         summary: generate_summary()
         keyword: keyword_analysis()
         similar_articles: web_search()
     }
      If user adds response key - returns specific response value'''
    user_id = request.args.get('user_id', type=UUID)
    document_id = request.args.get('document_id', type=UUID)

    session = get_my_session()

    try:
        # Query the database for the response based on user_id and document_id
        response = session.query(NLP_Response).filter_by(
            user_id=user_id, document_id=document_id).first()

        if response:
            # Construct the response dictionary
            response_data = {
                'user_uid': response.user_id,
                'document_id': response.document_id,
                'title': response.title_summary,
                'summary': response.title_summary,
                'keyword': response.keywords,
                'similar_articles': response.similar_articles
            }
            return response_data, 200
        return 'Response not found for the given user and document', 404
    except Exception as e:
        return f'Error reading responses: {str(e)}', 500
    finally:
        session.close()


@output_bp.route('/get_paragraphs', methods=['GET'])
def get_paragraph():
    '''  returns:
     Returns paragraph from document database depending on document id and paragraph id
      If user adds response key - returns specific response value

      '''

    document_id = request.args.get('document_id', type=UUID)

    # Get SQLAlchemy session using session factory function
    session = get_my_session()

    try:
        # Query paragraph from paragraph table
        paragraphs = session.query(Paragraphs).filter_by(id=document_id)
        # Turn query into list
        paragraphs = list(paragraphs)
        return  paragraphs

    except Exception as e:
        return f'Error fetching paragraph: {str(e)}', 500
    finally:
        session.close()
