import streamlit as st
from typing import List
from src.utils import Utils
from src.models.model import Model
from src.logger import Logger

# Streamlit Framework App for Multiple Documents Comparison
class App:
    def __init__(self) -> None:
        self.docs: List | None = None
        self.logger = Logger()
        self.utils = Utils()
        self.chat_groq = Model()
    
    def main(self) -> None:
        st.set_page_config("Compare Multiple PDFs Documents")
        st.header("AI-Powered Document Analyzer")
        
        self.docs = st.file_uploader("Upload your PDF files and click on the Submit & Process button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if len(self.docs) > 0:
                with st.spinner("Processing...."):
                    docs_dict = {}
                    for doc in self.docs:
                        file_name = doc.name
                        
                        if "pdf" in file_name:
                            try:
                                self.logger.log("App >> Getting the Documents Content")
                                raw_text = self.utils.get_documents_content(doc)
                            
                                # Process the text and clean them
                                self.logger.log("App >> Processing the Raw Text")
                                preprocessed_text = self.utils.process_the_raw_text(raw_text)
                                docs_dict[file_name] = preprocessed_text
                            except Exception as ex:
                                self.logger.log("Error occurred while processing the raw text from PDF documents.")
                                st.error(f"Something Went Wrong !")
                                return
                        else:
                            st.error("All the documents should be in PDF format!")
                            return
                    
                    try:
                        # Create a Prompt Template for compare multiple documents
                        self.logger.log("App >> Creating the Prompt Template")
                        compare_docs_chain = self.chat_groq.create_prompt_template()
                        
                        # Generate Response
                        self.logger.log("App >> Generating the response")
                        response = self.chat_groq.generate_response(compare_docs_chain, docs_dict)
                    except Exception as ex:
                        self.logger.log("Error occurred while generating the response.")
                        st.error(f"Something Went Wrong !")
                        return
                    
                    # Show the Response in Streamlit App
                    st.markdown(response, unsafe_allow_html=True)
            else:
                st.error("Please select atleast one document!", icon="🚨")

if __name__ == "__main__":
    # Instantiating the App Class
    app = App()
    app.main()