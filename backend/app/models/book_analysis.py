from typing import List, Tuple, Optional
from pydantic import BaseModel, Field

class AboutTheBook(BaseModel):
    book_title: str
    total_difficulty: int = Field(ge=1, le=10)
    chapter_amount: int

class Section(BaseModel):
    section_title: str
    section_number: int
    page_range: Tuple[int, int]
    key_concepts: List[str]
    estimated_reading_time_minutes: int

class ChapterAnalysis(BaseModel):
    chapter_number: int
    content_density: int = Field(ge=1, le=10)
    difficulty: int = Field(ge=1, le=10)
    pedagogic_objective_summary: str
    sections: List[Section]
    @property
    def total_reading_time(self) -> int:
        return sum(section.estimated_reading_time_minutes for section in self.sections)
    @property
    def core_concepts(self) -> List[str]:
        return sorted(
            set(
                concept
                for section in self.sections
                for concept in section.key_concepts
            )
         )


class ChapterOutline(BaseModel):
    chapter_name: str
    chapter_number: int
    page_range: Tuple[int, int]

class BookState(BaseModel):
    about_the_book: Optional[AboutTheBook] = None
    chapter_outline: Optional[List[ChapterOutline]] = None
    chapter_analyses: Optional[List[ChapterAnalysis]] = None



# old models
class Chapter(BaseModel):
    chapter_name: str
    chapter_number: int
    content_density: int = Field(ge=1, le=10)
    difficulty: int = Field(ge=1, le=10)
    page_range: Tuple[int, int]
    reading_time_minutes: int
    core_concepts: List[str]
    prerequirement_chapters: List[int]
    pedagogic_objective_brief_summary: str

class BookSchema(BaseModel):
    about_the_book: AboutTheBook
    chapters: List[Chapter]