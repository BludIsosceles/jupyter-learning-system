\"\"\"
ProgressTracker: Tracks student progress, completion status, and learning achievements.
\"\"\"

from typing import Dict, List, Any
from dataclasses import dataclass, field
from datetime import datetime
import json
from pathlib import Path


@dataclass
class LessonProgress:
    \"\"\"Tracks progress on a single lesson.\"\"\"
    lesson_id: str
    lesson_title: str
    started_at: str = field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None
    completion_percentage: int = 0
    quiz_score: Optional[int] = None
    challenges_completed: List[str] = field(default_factory=list)
    time_spent_minutes: int = 0
    
    @property
    def is_completed(self) -> bool:
        return self.completion_percentage >= 100


class ProgressTracker:
    \"\"\"Tracks overall student progress and achievements.\"\"\"
    
    def __init__(self, student_name: str):
        self.student_name = student_name
        self.lesson_progress: Dict[str, LessonProgress] = {}
        self.total_points: int = 0
        self.badges_earned: List[str] = []
        self.created_at = datetime.now().isoformat()
    
    def start_lesson(self, lesson_id: str, lesson_title: str) -> LessonProgress:
        \"\"\"Mark a lesson as started.\"\"\"
        progress = LessonProgress(
            lesson_id=lesson_id,
            lesson_title=lesson_title
        )
        self.lesson_progress[lesson_id] = progress
        return progress
    
    def complete_lesson(self, lesson_id: str, completion_percentage: int = 100,
                       quiz_score: Optional[int] = None) -> None:
        \"\"\"Mark a lesson as completed.\"\"\"
        if lesson_id not in self.lesson_progress:
            raise ValueError(f"Lesson {lesson_id} not started yet")
        
        progress = self.lesson_progress[lesson_id]
        progress.completion_percentage = completion_percentage
        progress.completed_at = datetime.now().isoformat()
        if quiz_score is not None:
            progress.quiz_score = quiz_score
    
    def update_time_spent(self, lesson_id: str, minutes: int) -> None:
        \"\"\"Update time spent on a lesson.\"\"\"
        if lesson_id in self.lesson_progress:
            self.lesson_progress[lesson_id].time_spent_minutes += minutes
    
    def add_challenge_completion(self, lesson_id: str, challenge_id: str) -> None:
        \"\"\"Record completion of a code challenge.\"\"\"
        if lesson_id in self.lesson_progress:
            if challenge_id not in self.lesson_progress[lesson_id].challenges_completed:
                self.lesson_progress[lesson_id].challenges_completed.append(challenge_id)
    
    def add_points(self, points: int, reason: str = \"\") -> None:
        \"\"\"Add gamification points.\"\"\"
        self.total_points += points
    
    def award_badge(self, badge_name: str) -> None:
        \"\"\"Award a badge to the student.\"\"\"
        if badge_name not in self.badges_earned:
            self.badges_earned.append(badge_name)
    
    def get_progress_summary(self) -> Dict[str, Any]:
        \"\"\"Get an overview of student progress.\"\"\"
        completed_lessons = sum(1 for p in self.lesson_progress.values() if p.is_completed)
        total_time = sum(p.time_spent_minutes for p in self.lesson_progress.values())
        avg_quiz_score = None
        
        quiz_scores = [p.quiz_score for p in self.lesson_progress.values() if p.quiz_score]
        if quiz_scores:
            avg_quiz_score = sum(quiz_scores) / len(quiz_scores)
        
        return {
            \"student_name\": self.student_name,
            \"total_lessons_started\": len(self.lesson_progress),
            \"total_lessons_completed\": completed_lessons,
            \"total_points\": self.total_points,
            \"total_time_minutes\": total_time,
            \"average_quiz_score\": avg_quiz_score,
            \"badges_earned\": len(self.badges_earned),
            \"badges\": self.badges_earned,
        }
    
    def export_progress(self, filepath: str) -> str:
        \"\"\"Export progress to JSON.\"\"\"
        progress_data = {
            \"student_name\": self.student_name,
            \"created_at\": self.created_at,
            \"summary\": self.get_progress_summary(),
            \"lesson_progress\": {
                lid: {
                    \"lesson_id\": p.lesson_id,
                    \"lesson_title\": p.lesson_title,
                    \"started_at\": p.started_at,
                    \"completed_at\": p.completed_at,
                    \"completion_percentage\": p.completion_percentage,
                    \"quiz_score\": p.quiz_score,
                    \"challenges_completed\": p.challenges_completed,
                    \"time_spent_minutes\": p.time_spent_minutes,
                }
                for lid, p in self.lesson_progress.items()
            }
        }
        
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, indent=2)
        
        return str(path.absolute())
