from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from enum import Enums

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client()

def upload_book(file_path: str):
    try:
        book = client.files.upload(file=file_path)
        return book.name
    except Exception as e:
        return str(e)

def gen_cache(book: str, ttl: int, display_n: str, gemini_model: Models):
    try:
        book_object = client.files.get(name=book)
        cache = client.caches.create(
            model=gemini_model,
            config=types.CreateCachedContentConfig(
                display_name=display_n
            )
            contents=[book_object],
            ttl=str(ttl) + "s",
        ),
        return display_n
    except Exception as e:
        return str(e)

def get_cache(cache_name: str):
    try:
        cache = client.caches.get(name=cache_name)
        return cache
    except Exception as e:
        return str(e)

def delete_cache(cache_name: str):
    try:
        client.caches.delete(name=cache_name)
        return "Cache deleted successfully."
    except Exception as e:
        return str(e)

