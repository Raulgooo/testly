import os
from typing import Annotated
from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import tempfile
import sqlite3
import models.book_analysis, models.macrocalendar, models.content_gen, models.user_constraints
import json
schema_1 = models.book_analysis.BookSchema
schema_2 = models.macrocalendar.StudySchedule
schema_3 = models.content_gen.WeeklyStudyPlan
schema_4 = models.user_constraints.UserConstraints
user_style = models.user_constraints.UserStyle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
app = FastAPI()
client = genai.Client()
prompts = []

with open("prompts/book_analysis.md", 'r') as file:
    prompts.append(file.read())

with open("prompts/macrocalendar.md", 'r') as file:
    prompts.append(file.read())

with open("prompts/the_content_engine.md", 'r') as file:
    prompts.append(file.read())





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

@app.get("/process_book")
async def process_book(book):
  book = client.files.get(name="files/gah8gt9ehkjk")
  response = client.models.generate_content(
    model="gemini-2.5-flash", contents=[prompts[0], book], config=
    {
      "response_mime_type": "application/json",
      "response_json_schema": schema_1.model_json_schema(),
    }
)
  book_structure = schema_1.model_validate_json(response.text)
  return book_structure

@app.post("/generate_macrocalendar")
async def generate_macrocalendar(book_structure):
  book = client.files.get(name="files/gah8gt9ehkjk")
  USER_CONSTRAINTS_MOCK = """
{
  "daily_study_time_min": 150,
  "study_days_per_week": 6,
  "course_duration_weeks": 16,
  "exams": [
    {
      "exam_week": 8,
      "exam_topics": [
        "Sistemas de ecuaciones",
        "Matrices y Determinantes",
        "Espacios Vectoriales"
      ],
      "exam_type": "partial"
    },
    {
      "exam_week": 16,
      "exam_topics": [
        "Todo el contenido del semestre",
        "Transformaciones Lineales",
        "Autovalores y Autovectores"
      ],
      "exam_type": "accumulative"
    }
  ]
}
"""
  prompt_macrocalendar = prompts[1].replace("{{BOOK_STRUCTURE}}", book_structure)
  prompt_macrocalendar = prompt_macrocalendar.replace("{{USER_CONSTRAINTS}}", USER_CONSTRAINTS_MOCK)
  #prompt_macrocalendar = prompt_macrocalendar.replace("{{BOOK_PDF}}", book)

  response = client.models.generate_content(
    model="gemini-2.5-flash", contents=[prompt_macrocalendar, book], config=
    {
      "response_mime_type": "application/json",
      "response_json_schema": schema_2.model_json_schema(),
    }
)
  study_schedule = schema_2.model_validate_json(response.text)
  return study_schedule

@app.post("/generate_weekly_plan")
async def generate_weekly_plan(study_schedule: Annotated[str, Form()], target_week_number: Annotated[int, Form()], user_style_preferences:  Annotated[user_style, Form()]):
  book = client.files.get(name="files/gah8gt9ehkjk")
  prompt_content_engine = prompts[2].replace("{{MACRO_CALENDAR_JSON}}", study_schedule)
  prompt_content_engine = prompt_content_engine.replace("{{TARGET_WEEK}}", str(target_week_number))
  prompt_content_engine = prompt_content_engine.replace("{{USER_STYLE}}", user_style_preferences)
  response = client.models.generate_content(
    model="gemini-2.5-flash", contents=[prompt_content_engine, book], config=
    {
      "response_mime_type": "application/json",
      "response_json_schema": schema_3.model_json_schema(),
    }
)
  weekly_study_plan = schema_3.model_validate_json(response.text)
  return weekly_study_plan



#nombre_del_archivo = "files/roeqq5tzltyn"
#myfile = client.files.get(name=nombre_del_archivo)



