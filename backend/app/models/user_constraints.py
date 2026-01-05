from pydantic import BaseModel, Field
from typing import List, Tuple
from enum import Enum

class ExamType(str, Enum):
    ACCUMULATIVE = "accumulative"
    PARTIAL = "partial"

class ExamDetails(BaseModel):
    exam_week: int = Field(..., ge=1, le=52)
    exam_topics: List[str]
    exam_type: ExamType

class UserConstraints(BaseModel):
    daily_study_time_min: int = Field(..., gt=0, le=720) 
    study_days_per_week: int = Field(..., ge=1, le=7)
    course_duration_weeks: int = Field(..., ge=1, le=52)
    exams: List[ExamDetails]
    book_scope: Tuple[int, int]

class UserStyle(str, Enum):
    ACADEMIC = "academic"
    BALANCED = "balanced"
    SIMPLFIIED = "simplified"