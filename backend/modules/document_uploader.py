'''This module manages uploading and ingestion of files/pdfs'''
from uuid import uuid4, uuid1
from datetime import datetime
from flask import Blueprint, request
from modules.tables import Documents, Paragraphs
from session_factory import get_my_session
SIZE_LIMIT = 500  # sample size limit in megabytes

document_db = Blueprint('document_db', __name__)


def create_paragraph(text, document_id):
    '''Creates paragraph in database'''
    try:
        session = get_my_session()
        document = Paragraphs(document_id=document_id, text=text)
        session.add(document)
        session.commit()
        return 'Response created successfully', 200
    except Exception as e:
        return f'Error creating response: {str(e)}', 500


@document_db.route('/create_document',methods=['POST'])
def create_document():
    '''Recieves document as pdf, etc, or as URL/html and parses into text, uploading to document db'''
    file = request.files['file']

    filename = file.name           # Gives name
    filetype = file.content_type   # Gives Content type text/html etc
    read = file.read()
    # if size > SIZE_LIMIT:
    #     return 'File limit exceeded', 403

    if filetype == 'docx':
        def parse_docx(read):
            '''Parses Microsoft document uploads'''
    if filetype == 'pdf':
        def parse_pdf(read):
            '''Parses pdf uploads'''
    if filetype == 'html':
        def scrape_url(read):
            '''Scrapes html from url and generates text output'''
    def split_paragraphs():
        '''Splits paragraphs by AI or just analysis of newlines'''
        return ['hello', 'world']
    print(read.decode())
    try:
        session = get_my_session()
        document = Documents(document_name=filename, uploaded_on=datetime.now(
        ), filetype=filetype, fulltext=read.decode())
        session.add(document)
        # Split fulltext into paragraphs and send each paragraph to the database
        paragraphs = split_paragraphs()
        for paragraph in paragraphs:
            create_paragraph(paragraph, document.document_id)
        session.commit()
        session.refresh(document)
        doc_id = document.document_id
        return {"document_id" : doc_id}, 201
    except Exception as e:
        return f'Error creating response: {str(e)}', 500
