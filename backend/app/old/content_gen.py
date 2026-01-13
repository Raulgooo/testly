from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

# --- Enums ---

class BlockType(str, Enum):
    LECTURE = "lecture_block"
    PRACTICE = "practice_block"
    QUIZ = "theory_quiz_block"

# --- Component Models ---

class SourceMapping(BaseModel):
    page_number: Optional[int] = None
    citation_anchor: Optional[str] = None

class Slide(BaseModel):
    title: Optional[str] = None
    content_text: Optional[str] = None
    latex_formula: Optional[str] = None
    source_mapping: Optional[SourceMapping] = None

class ExerciseSolution(BaseModel):
    final_answer: Optional[str] = None
    step_by_step: Optional[str] = None
    latex_steps: Optional[str] = None

class Exercise(BaseModel):
    exercise_id: Optional[str] = None
    problem_statement: Optional[str] = None
    solution: Optional[ExerciseSolution] = None

class QuizOption(BaseModel):
    id: Optional[str] = None
    text: Optional[str] = None

class QuizQuestion(BaseModel):
    question_text: Optional[str] = None
    options: Optional[List[QuizOption]] = None
    correct_option_id: Optional[str] = None

# --- Main Structure ---

class LearningBlock(BaseModel):
    type: BlockType
    theme: Optional[str] = None
    # Depending on 'type', one of these will be populated
    slides: Optional[List[Slide]] = None
    exercises: Optional[List[Exercise]] = None
    questions: Optional[List[QuizQuestion]] = None

class StudyDay(BaseModel):
    day_number: int
    day_title: str
    is_rest_day: bool = False
    learning_blocks: List[LearningBlock]

class WeeklyStudyPlan(BaseModel):
    week_number: int
    weekly_focus_theme: str
    days: List[StudyDay]