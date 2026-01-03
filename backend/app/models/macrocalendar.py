from typing import List, Tuple, Optional
from enum import Enum
from pydantic import BaseModel, Field

# --- Enums for strict string options ---

class StudyPhase(str, Enum):
    BASE = "Base"
    BUILD = "Build"
    DELOAD = "Deload"
    PEAK = "Peak"
    TAPER = "Taper"
    POST_SEASON = "Post-Season"

class ActivityType(str, Enum):
    THEORY_PRACTICE = "Theory + Practice"
    PRACTICE_ONLY = "Practice Only"
    ACTIVE_RECALL = "Active Recall"
    MOCK_EXAM = "Mock Exam"
    REST = "Rest"

# --- Models ---

class DayPlan(BaseModel):
    day_number: int
    topic: str
    target_chapter_id: Optional[int] = None
    # Enforces exactly 2 integers: [start_page, end_page]
    pages: Tuple[int, int]
    activity_type: ActivityType
    reasoning: str

class WeekPlan(BaseModel):
    week_number: int
    phase: StudyPhase
    days: List[DayPlan]

class PlanOverview(BaseModel):
    total_weeks: int
    pacing_strategy: str

class StudySchedule(BaseModel):
    plan_overview: PlanOverview
    weeks: List[WeekPlan]
