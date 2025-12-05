import base64
import requests
import io
import PIL import Image
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions -s \"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the .env file")

if __name__=="__main__":
    image_path = "path/to/your/image.jpg"
    query="what are the encoders in this picture?"
    result=process_image(image_path, query)
    print (result)
