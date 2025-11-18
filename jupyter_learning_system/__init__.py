# Jupyter Learning System
# A comprehensive system for generating educational Jupyter notebooks and learning materials
# for children, with gamification, progress tracking, and interactive exercises.

__version__ = "0.1.0"
__author__ = "Justin Crawford"
__description__ = "Educational notebook generation system for kids"

from jupyter_learning_system.generators.notebook_generator import NotebookGenerator
from jupyter_learning_system.curriculum.curriculum_manager import CurriculumManager
from jupyter_learning_system.progress.tracker import ProgressTracker
from jupyter_learning_system.gamification.badges import BadgeSystem

__all__ = [
    "NotebookGenerator",
    "CurriculumManager", 
    "ProgressTracker",
    "BadgeSystem",
]
