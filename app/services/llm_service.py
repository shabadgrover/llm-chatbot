from langchain_core import messages
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class LLMService:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model_name = os.getenv("MODEL_NAME")

        self.llm = ChatGroq(
            model=self.model_name,
            api_key=self.api_key
        )
    
    def get_response(self, messages):
        response = self.llm.invoke(messages)

        return {
            "response": response.content,
            "usage": response.usage_metadata
        }