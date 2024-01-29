from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# access openAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
