from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

class GroqLLm:

    def get_llm(self):
        try:
            api_key=os.getenv('GROQ_API_KEY')
            model=ChatGroq(model='openai/gpt-oss-120b',streaming=False,temperature=0,api_key=api_key)
            return model
        except Exception as e:
            raise ValueError(e)