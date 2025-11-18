"""
Example: Creating a Python Basics Lesson for Kids
Demonstrates how to use the jupyter-learning-system to create engaging lessons.
"""

from jupyter_learning_system import (
    NotebookGenerator, 
    CurriculumManager, 
    Lesson, 
    LevelDifficulty,
    ProgressTracker,
    BadgeSystem
)


def create_python_hello_world_lesson():
    """Create a fun introductory lesson about printing in Python."""
    
    # Initialize notebook
    notebook = NotebookGenerator(
        title="Hello, Python!",
        description="Your first Python program",
        author="Junior Programming Teacher"
    )
    
    # Add title and introduction
    notebook.set_title_and_intro(
        "🐍 Hello, Python!",
        "Welcome, young programmer! Let's learn how to make Python say hello! 👋"
    )
    
    # Add a fun fact
    notebook.add_fun_fact(
        "Python is named after the British comedy group Monty Python, not the snake! 🎭"
    )
    
    # Add learning objectives
    notebook.add_markdown_cell(
        "## 🎯 What You'll Learn\n\n"
        "- What the `print()` function does\n"
        "- How to display text on your screen\n"
        "- How to run your first Python program\n"
    )
    
    # First code example
    notebook.add_markdown_cell("## 💻 Your First Program")
    notebook.add_code_cell(
        "print('Hello, World!')\n"
        "print('Welcome to Python!')\n"
        "print('🚀 I am learning to code!')"
    )
    
    # Add a quiz
    notebook.add_quiz_cell(
        "What will the print() function do?",
        [
            "Display text on the screen",
            "Make the computer beep",
            "Create a new file",
            "Print something on paper"
        ],
        correct_index=0,
        explanation=(
            "Perfect! The `print()` function displays whatever text you put between "
            "the parentheses on your screen. It's like telling Python to show something!"
        )
    )
    
    # Visual exercise
    notebook.add_visual_exercise(
        "Make Your Own Message",
        "Try modifying the print statements to display YOUR name and favorite emoji!",
        visual_type="ascii_art"
    )
    
    # Challenge
    notebook.add_challenge_cell(
        "Create Your Own Print Messages",
        "Write 3 print() statements that display:\n"
        "1. Your name\n"
        "2. Your favorite animal\n"
        "3. A fun fact about yourself",
        starter_code="# Write your 3 print statements here:\n"
                     "print('Your name here')\n"
                     "print('Your animal here')\n"
                     "print('Your fact here')",
        hints=[
            "Remember to use quotes around your text",
            "Each print() statement should be on a new line",
            "You can add emojis! 🎉"
        ]
    )
    
    # Fun facts
    notebook.add_fun_fact(
        "Did you know? You can use emojis in print statements! "
        "Try `print('🎮 Gaming is fun!')`"
    )
    
    # Summary
    notebook.add_markdown_cell(
        "## ✅ You Did It!\n\n"
        "Great job! You've learned how to use the `print()` function. "
        "This is the foundation of every Python program! 🎉\n\n"
        "**Next Steps:** Try writing more complex print statements with different messages."
    )
    
    # Save the notebook
    notebook.save("examples/python_hello_world.ipynb")
    print("✅ Lesson saved to: examples/python_hello_world.ipynb")


def create_sample_curriculum():
    """Create a sample Python curriculum for young learners."""
    
    curriculum = CurriculumManager("🐍 Python for Young Coders (Ages 8-12)")
    
    # Create Python Basics Module
    python_basics = curriculum.create_module(
        "python_basics",
        "Python Basics",
        "Learn the fundamentals of Python programming"
    )
    
    # Define lessons
    lessons = [
        Lesson(
            id="python_hello",
            title="Hello, Python!",
            description="Your first Python program using print()",
            topic="Python",
            difficulty=LevelDifficulty.BEGINNER,
            estimated_duration_minutes=15,
            learning_outcomes=[
                "Understand what Python is",
                "Use the print() function",
                "Run your first program"
            ],
            gamification_points=100,
        ),
        Lesson(
            id="python_variables",
            title="Variables and Data Types",
            description="Learn how to store and use information",
            topic="Python",
            difficulty=LevelDifficulty.BEGINNER,
            estimated_duration_minutes=20,
            prerequisites=["python_hello"],
            learning_outcomes=[
                "Create variables",
                "Understand data types (string, int, float)",
                "Use variables in print statements"
            ],
            gamification_points=150,
        ),
        Lesson(
            id="python_input",
            title="Getting User Input",
            description="Make your programs interactive!",
            topic="Python",
            difficulty=LevelDifficulty.BEGINNER,
            estimated_duration_minutes=20,
            prerequisites=["python_variables"],
            learning_outcomes=[
                "Use the input() function",
                "Store user responses",
                "Create interactive programs"
            ],
            gamification_points=150,
        ),
    ]
    
    # Add lessons to curriculum
    for lesson in lessons:
        curriculum.add_lesson("python_basics", lesson)
    
    # Export curriculum
    curriculum.export_curriculum("examples/curriculum_kids.json")
    
    # Show overview
    overview = curriculum.get_curriculum_overview()
    print(f"\n✅ Curriculum created!")
    print(f"   Modules: {overview['total_modules']}")
    print(f"   Lessons: {overview['total_lessons']}")
    print(f"   Saved to: examples/curriculum_kids.json")


def track_student_progress():
    """Example of tracking a student's progress."""
    
    # Create progress tracker for a student
    tracker = ProgressTracker("Emma")
    
    # Start first lesson
    tracker.start_lesson("python_hello", "Hello, Python!")
    
    # Simulate completing lesson
    tracker.complete_lesson("python_hello", completion_percentage=100, quiz_score=95)
    tracker.update_time_spent("python_hello", 18)  # 18 minutes
    tracker.add_challenge_completion("python_hello", "challenge_1")
    tracker.add_points(100, "Completed Python Basics lesson")
    tracker.award_badge("first_lesson")
    
    # Show progress
    summary = tracker.get_progress_summary()
    print(f"\n✅ Progress Tracking:")
    print(f"   Student: {summary['student_name']}")
    print(f"   Lessons Completed: {summary['total_lessons_completed']}")
    print(f"   Total Points: {summary['total_points']}")
    print(f"   Badges: {', '.join(summary['badges'])}")
    
    # Export progress
    tracker.export_progress("examples/emma_progress.json")
    print(f"   Progress saved to: examples/emma_progress.json")


def show_badge_system():
    """Display the badge system."""
    
    badge_system = BadgeSystem()
    print(f"\n🏆 Available Badges:\n")
    
    for badge in badge_system.get_all_badges():
        print(f"   {badge_system.get_badge_display(badge)}")


if __name__ == "__main__":
    print("🎓 Jupyter Learning System - Example Demonstrations\n")
    print("=" * 60)
    
    # Run examples
    create_python_hello_world_lesson()
    print()
    create_sample_curriculum()
    print()
    show_badge_system()
    print()
    track_student_progress()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed successfully!")
