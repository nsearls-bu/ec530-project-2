'''This module manages uploading and ingestion of files/pdfs'''
from uuid import uuid4, UUID
from flask import Blueprint, request

SIZE_LIMIT = 500  # sample size limit in megabytes

document_db = Blueprint('document_db', __name__)


@document_db.route('/create_document')
def create_document():
    '''Recieves document as pdf, etc, or as URL/html and parses into text, uploading to document db'''

    file = request.FILES['filename']
    filename = file.name           # Gives name
    filetype = file.content_type   # Gives Content type text/html etc
    size = file.size           # Gives file's size in byte
    read = file.read()

    if size > SIZE_LIMIT:
        return 'File limit exceeded', 403

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
        pass

    def create_parsed_document(filename, read, filetype):
        '''Write to document table
        document_id : id,
        full_text: {paragraph_1: paragraph_1_text ...}
        '''
        split_paragraphs()
        res = 'WRITE TO DB'
        return res
    res = create_parsed_document(filename, read, filetype)

    if res is not None:
        return res, 200
    return 400
