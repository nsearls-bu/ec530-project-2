'''Does basic NLP analysis of text input'''

def create_engine_connection(name, url):
    '''
    Connects to container managing NLP processing or website API
    {'connection_name' : name
    connection_url: url
    connection_type: website API or other NLP processor}
    writes to connection table in table
    '''

def create_response(user_uid, document_id):
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
    # Input text fetched from document table
    def generate_summary(input_text):
        '''Uses prompt like "generate a summary of the following text"'''
    def title_summary(input_text):
        '''Generate a single sentence summary'''
    def generate_sentiment(input_text):
        '''Uses prompt like "Assess the overall sentiment of the following text on a scale of 1-5 where 1 is most negative and 5 is most positive"'''
    def keyword_analysis(input_text):
        '''Uses prompt like "Generate 15 keywords from the following text with definitions as key-pairs in a json'''
    def proper_noun_analysis(input_text):
        '''Record every proper noun in this document and output a list of names,locations, institutions, and addresses'''
    def web_search():
        '''Crafts a google search based on a keywords, summary, and article title - returns web links'''

def create_document():
    '''Write to document table
    document_id : id,
    full_text: {paragraph_1: paragraph_1_text ...}
    '''
    def split_paragraphs():
        '''Splits paragraphs by AI or just analysis of newlines'''
        pass
def search_document(document_id, keyword):
    '''Searches documents and returns paragraph of document that best fits keyword'''