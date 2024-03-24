'''Contains function used to create PDF processing worker'''
from io import BytesIO
import pdfreader

with open('pdf_tests/AAIC-Abstract-Submission-Guidelines.pdf', "rb") as f:
    stream = BytesIO(f.read())

def pdf_extract_text(pdf_input: BytesIO):
    '''Extracts PDF input and writes text to DB'''
    viewer = pdfreader.SimplePDFViewer(pdf_input)
    
    for canvas in viewer:
        print(canvas)
pdf_extract_text(stream)