from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

google_client = genai.Client()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

book = google_client.files.get(name="files/gah8gt9ehkjk")

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe el libro proporcionado por favor."},
        {
            "type": "media",
            "file_uri": book.uri,        # La URI de Google Cloud Storage
            "mime_type": book.mime_type  # El tipo de archivo (ej: application/pdf)
        },
    ]
)

response = model.invoke([message])
print(response.content)