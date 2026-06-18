from dotenv import load_dotenv
import os

load_dotenv()

print("API Key Found:", bool(os.getenv("GROQ_API_KEY")))
print("Model Name:", os.getenv("MODEL_NAME"))