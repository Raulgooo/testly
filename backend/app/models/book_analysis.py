from typing import List, Tuple
from pydantic import BaseModel, Field

class AboutTheBook(BaseModel):
    book_title: str
    total_difficulty: int = Field(ge=1, le=10)
    chapter_amount: int

class Chapter(BaseModel):
    chapter_name: str
    chapter_number: int
    content_density: int = Field(ge=1, le=10)
    difficulty: int = Field(ge=1, le=10)
    # Using Tuple[int, int] enforces exactly 2 items as per minItems/maxItems
    page_range: Tuple[int, int]
    reading_time_minutes: int
    core_concepts: List[str]
    prerequirement_chapters: List[int]
    pedagogic_objective_brief_summary: str

class BookSchema(BaseModel):
    about_the_book: AboutTheBook
    chapters: List[Chapter]