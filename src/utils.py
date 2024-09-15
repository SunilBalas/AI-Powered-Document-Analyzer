from pathlib import Path
from PyPDF2 import PdfReader
import spacy
import re
import sys
from src.logger import Logger
from src.exception import CustomException

# Helper class for the App
class Utils:
    def __init__(self) -> None:
        self.logger = Logger()
        self.nlp = self.load_spacy_model()
        
    def load_spacy_model(self):
        try:
            self.logger.log("Utils >> Loading the Spacy English Small Model")
            nlp = spacy.load("en_core_web_sm")
            return nlp
        except Exception as ex:
            raise CustomException(ex, sys)
    
    # fetch pdf docs and get the text
    def get_documents_content(self, doc: Path) -> str:
        try:
            text = ""
            self.logger.log("Utils >> Reading the PDF Document and Extracting the texts")
            pdf_reader = PdfReader(doc)
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as ex:
            raise CustomException(ex, sys)
    
    # process the raw text using nlp techniques
    def process_the_raw_text(self, raw_text: str) -> str:
        try:
            doc = self.nlp(raw_text)
            tokens = []
            
            self.logger.log("Utils >> Processing the Raw Texts using NLP Techniques")
            for token in doc:
                if not token.is_stop and not token.is_punct and re.compile(r'^[a-zA-Z0-9]*$').match(str(token)):
                    tokens.append(str(token))
                    
            return (" ".join(tokens)).lower()
        except Exception as ex:
            raise CustomException(ex, sys)