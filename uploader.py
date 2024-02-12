'''This module manages uploading and ingestion of files/pdfs'''

def create_document():
    '''Recieves document as pdf, etc, or as URL/html and parses into text, uploading to document db'''
    def parse_pdf():
        '''Parses pdf uploads'''
    def parse_docx():
        '''Parses Microsoft document uploads'''
    def scrape_url():
        '''Scrapes html from url and generates text output'''

    def create_parsed_document():
        '''Write to document table
        document_id : id,
        full_text: {paragraph_1: paragraph_1_text ...}
        '''
    def split_paragraphs():
        '''Splits paragraphs by AI or just analysis of newlines'''
        pass