import os
from typing import Annotated
from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import tempfile
import sqlite3

user_style = models.user_constraints.UserStyle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
app = FastAPI()
client = genai.Client()
prompts = []


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/uploadbook/")

