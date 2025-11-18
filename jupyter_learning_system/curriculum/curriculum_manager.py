\"\"\"
CurriculumManager: Manages lesson progression, dependencies, and curriculum structure.
Organizes lessons into coherent learning paths with prerequisites and sequencing.
\"\"\"

from typing import List, Dict, Any, Optional
from enum import Enum
from dataclasses import dataclass, field
import json
from pathlib import Path


class LevelDifficulty(Enum):
    \"\"\"Difficulty levels for lessons.\"\"\"
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


@dataclass
class Lesson:
    \"\"\"Represents a single lesson in the curriculum.\"\"\"
    id: str
    title: str
    description: str
    topic: str
    difficulty: LevelDifficulty
    estimated_duration_minutes: int = 15
    prerequisites: List[str] = field(default_factory=list)
    learning_outcomes: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    gamification_points: int = 100
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "topic": self.topic,
            "difficulty": self.difficulty.name,
            "estimated_duration_minutes": self.estimated_duration_minutes,
            "prerequisites": self.prerequisites,
            "learning_outcomes": self.learning_outcomes,
            "tags": self.tags,
            "gamification_points": self.gamification_points,
        }


@dataclass
class Module:
    \"\"\"Groups related lessons into a module.\"\"\"
    id: str
    title: str
    description: str
    lessons: List[Lesson] = field(default_factory=list)
    
    def add_lesson(self, lesson: Lesson) -> 'Module':
        \"\"\"Add a lesson to this module.\"\"\"
        self.lessons.append(lesson)
        return self


class CurriculumManager:
    \"\"\"Manages the overall curriculum structure and lesson progression.\"\"\"
    
    def __init__(self, name: str = "Kid's Learning Curriculum"):
        self.name = name
        self.modules: Dict[str, Module] = {}
        self.lessons: Dict[str, Lesson] = {}
        self.lesson_graph: Dict[str, List[str]] = {}  # dependency graph
    
    def create_module(self, module_id: str, title: str, description: str) -> Module:
        \"\"\"Create a new module.\"\"\"
        module = Module(id=module_id, title=title, description=description)
        self.modules[module_id] = module
        return module
    
    def add_lesson(self, module_id: str, lesson: Lesson) -> None:
        \"\"\"Add a lesson to a module.\"\"\"
        if module_id not in self.modules:
            raise ValueError(f"Module {module_id} not found")
        
        self.modules[module_id].add_lesson(lesson)
        self.lessons[lesson.id] = lesson
        
        # Initialize dependency tracking
        if lesson.id not in self.lesson_graph:
            self.lesson_graph[lesson.id] = lesson.prerequisites
    
    def get_learning_path(self, start_lesson_id: str) -> List[str]:
        \"\"\"Get a recommended learning path starting from a lesson.\"\"\"
        path = []
        visited = set()
        
        def traverse(lesson_id: str):
            if lesson_id in visited:
                return
            visited.add(lesson_id)
            
            if lesson_id in self.lessons:
                # Visit prerequisites first
                lesson = self.lessons[lesson_id]
                for prereq in lesson.prerequisites:
                    traverse(prereq)
            
            path.append(lesson_id)
        
        traverse(start_lesson_id)
        return path
    
    def get_lesson_by_id(self, lesson_id: str) -> Optional[Lesson]:
        \"\"\"Retrieve a lesson by ID.\"\"\"
        return self.lessons.get(lesson_id)
    
    def get_lessons_by_difficulty(self, difficulty: LevelDifficulty) -> List[Lesson]:
        \"\"\"Get all lessons of a specific difficulty level.\"\"\"
        return [l for l in self.lessons.values() if l.difficulty == difficulty]
    
    def get_lessons_by_topic(self, topic: str) -> List[Lesson]:
        \"\"\"Get all lessons for a specific topic.\"\"\"
        return [l for l in self.lessons.values() if l.topic == topic]
    
    def export_curriculum(self, filepath: str) -> str:
        \"\"\"Export curriculum structure to JSON.\"\"\"
        curriculum_data = {
            "name": self.name,
            "modules": {
                m_id: {
                    "title": mod.title,
                    "description": mod.description,
                    "lessons": [les.to_dict() for les in mod.lessons]
                }
                for m_id, mod in self.modules.items()
            }
        }
        
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(curriculum_data, f, indent=2)
        
        return str(path.absolute())
    
    def get_curriculum_overview(self) -> Dict[str, Any]:
        \"\"\"Get a summary of the curriculum.\"\"\"
        return {
            "name": self.name,
            "total_modules": len(self.modules),
            "total_lessons": len(self.lessons),
            "modules": {
                m_id: {
                    "title": mod.title,
                    "lesson_count": len(mod.lessons)
                }
                for m_id, mod in self.modules.items()
            }
        }
