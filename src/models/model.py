# Langchain Chat Groq Configuration

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from typing import Any, Dict
from ..config import config
from ..logger import Logger

class Model:
    def __init__(self) -> None:
        self.config = config
        self.logger = Logger()
        self.llm = ChatGroq(
            model=self.config["model"],
            temperature=0,
            groq_api_key=self.config["groq_api_key"]
        )
    
    def create_prompt_template(self) -> Any:
        # Define a multiple documents comparison prompt template
        self.logger.log("Model >> Creating the Prompt Template")
        compare_docs_prompt_template = PromptTemplate.from_template(
            """
            ## DOCUMENTS FOR COMPARISON:
                - List of Documents Content:
                    - {document_dict}

            ==================================================================

            ## INSTRUCTIONS:
            
            - If user provides only one document then provide only Summary and Key Insights, 
            - DO NOT PROVIDE SIMILARITIES AS WELL AS PREAMBLE.
            - If user provides only one document then do not give response as document 1, etc., as only one document is provided.
            - Treat this response as a markdown file.

            Summary:
                - Provide a concise summary of each document from given document dictionary values, capturing the main points and overall message.
                - In your response, include the dictionary key as the document name, followed by the summary of the corresponding value.
                - Format:
                    **Document Name**: 
                        - [Summary of the document]

            ===================================================================

            Similarities:
                - Identify and describe the similarities across the documents. Focus on common themes, topics, or pieces of information.

            ===================================================================

            Key Insights:
                - Extract and list key pieces of information from each document, such as, specific places or regions mentioned, any organizations or entities referenced, notable facts, data, or events, mentioned individuals or relevant people, etc. 
                - If any of the mentioned things are present in the document then give the yellow as background color and black as font color to that word, also wrap the word into rounded border of 3 pixel.
                - If any of the mentioned things are not present in the document then do not include them as response.
                
                - In your response, include the dictionary key as the document name, followed by the key insights of the corresponding value.
                - Format:
                    **Document Name**: 
                        - [Key insights of the document]

            ## EXAMPLE RESPONSE:

            ### Summary:
            
                - **Document Name**: 
                    - [Summary]
                    

            ### Similarities:
            
                - [List of similarities]
                

            ### Key Insights:
            
                - **Document Name**: 
                    - [Key Insights]
                
            """
        )

        compare_docs_chain = compare_docs_prompt_template | self.llm
        return compare_docs_chain

    def generate_response(self, chain: Any, docs:Dict[str, str]) -> str:
        self.logger.log("Model >> Generating the response from the Llama Model")
        response = chain.invoke(
            {
                "document_dict": docs
            }
        )
        return response.content