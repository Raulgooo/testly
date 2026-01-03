import os
from typing import Annotated
from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import tempfile
import sqlite3

import models.book_analysis, models.macrocalendar, models.content_gen

schema_1 = models.book_analysis.BookSchema
schema_2 = models.macrocalendar.StudySchedule
schema_3 = models.content_gen.WeeklyStudyPlan

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
app = FastAPI()
client = genai.Client()




@app.get("/")
def h():
  print("hello world")
  return print("hello")

@app.post("/upload_book")
async def upload_book(
  book_info: Annotated[str, Form()],
  pdf_file: Annotated[UploadFile, File()]
):
    try:
      file_content = await pdf_file.read()
      with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, pdf_file.filename)
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(file_content)
            book = client.files.upload(file=temp_file_path)
        return book
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def process_book():
  response = client.models.generate_content(
    model="gemini-2.5-flash", contents=["Describe this audio clip", myfile]
)



#nombre_del_archivo = "files/roeqq5tzltyn"
#myfile = client.files.get(name=nombre_del_archivo)



