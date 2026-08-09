from google import genai
import os
from dotenv import load_dotenv

class GeminiClientFactory:

    def __init__(self):
        load_dotenv()

    def get_api_key(self)->str:
        api_key=os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing")

        return api_key

    def create_client(self)->genai.Client:

        api_key=self.get_api_key()
        client = genai.Client(api_key=api_key)

        return client
