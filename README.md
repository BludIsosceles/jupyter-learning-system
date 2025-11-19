# Jupyter Learning System 🎓

A comprehensive Python library and CLI tool for generating interactive, fun, and educational Jupyter Notebooks and learning materials for children. Perfect for teaching Python, JSON, Command Prompt, Linux, and other programming concepts.

## Features ✨

- **📔 Programmatic Notebook Generation**: Create beautiful Jupyter notebooks from Python code
- **🎯 Interactive Content**: Built-in support for quizzes, code challenges, and visual exercises
- **🏆 Gamification System**: Badges, points, and achievement tracking to keep learning fun
- **📊 Progress Tracking**: Monitor student progress with detailed metrics
- **📚 Curriculum Management**: Organize lessons into modules with prerequisites and dependencies
- **🖼️ Kid-Friendly Design**: Colorful emojis, playful language, and age-appropriate exercises
- **🔄 Multiple Output Formats**: Jupyter Notebooks, Markdown guides, HTML, and downloadable scripts

## Quick Start 🚀

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/jupyter-learning-system.git
cd jupyter-learning-system

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Basic Usage

#### Create a Simple Notebook

```python
from jupyter_learning_system import NotebookGenerator

# Create a new notebook
notebook = NotebookGenerator(
    title="My First Python Lesson",
    author="Your Name"
)

# Add content
notebook.set_title_and_intro(
    "My First Python Lesson",
    "Let's start our Python journey! 🚀"
)

# Add code cell
notebook.add_code_cell("print('Hello, World!')")

# Add a quiz
notebook.add_quiz_cell(
    "What will this code print?",
    ["Hello, World!", "Error", "Nothing"],
    correct_index=0,
    explanation="The print() function displays text on the screen."
)

# Add a challenge
notebook.add_challenge_cell(
    "Your First Challenge",
    "Try changing the message in the print statement.",
    "print('Hello, World!')",
    hints=["Modify the text between the quotes"]
)

# Save the notebook
notebook.save("my_first_lesson.ipynb")
```

#### Use the CLI

```bash
# Create a new student progress tracker
jupyter-learning init-student --name "Tommy"

# Generate a curriculum structure
jupyter-learning create-curriculum --output curriculum.json

# Show all available badges
jupyter-learning show-badges

# Create a custom lesson
jupyter-learning generate-lesson \
  --lesson python_intro \
  --title "Introduction to Python" \
  --output python_intro.ipynb
```

## Project Structure 📂

```
jupyter-learning-system/
├── jupyter_learning_system/
│   ├── generators/          # Notebook generation engine
│   │   └── notebook_generator.py
│   ├── curriculum/          # Curriculum management
│   │   └── curriculum_manager.py
│   ├── progress/            # Progress tracking
│   │   └── tracker.py
│   ├── gamification/        # Badge system & gamification
│   │   └── badges.py
│   ├── cli/                 # Command-line interface
│   │   └── main.py
│   ├── templates/           # Lesson templates (extensible)
│   └── __init__.py
├── examples/                # Example lessons and notebooks
├── data/                    # Sample data files
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Core Components

### 1. **NotebookGenerator**
The heart of the system. Programmatically creates Jupyter notebooks with:
- Markdown cells (text, descriptions)
- Code cells (Python code to execute)
- Quiz cells (interactive questions with explanations)
- Challenge cells (coding exercises with hints)
- Visual exercises (ASCII art, drawings)
- Fun facts and learning nuggets

```python
from jupyter_learning_system import NotebookGenerator

gen = NotebookGenerator("My Lesson")
gen.add_markdown_cell("# Welcome!")
gen.add_code_cell("print('Hello')")
gen.add_quiz_cell("Question?", ["Option A", "Option B"], correct_index=0)
gen.save("lesson.ipynb")
```

### 2. **CurriculumManager**
Organize lessons into a structured learning path:
- Create modules (groupings of related lessons)
- Define lessons with difficulty levels
- Set prerequisites and dependencies
- Generate learning paths
- Export curriculum structure

```python
from jupyter_learning_system import CurriculumManager, Lesson, LevelDifficulty

curriculum = CurriculumManager("Python Basics")
python_module = curriculum.create_module(
    "python_basics",
    "Python Fundamentals",
    "Learn Python from scratch"
)

lesson = Lesson(
    id="hello_python",
    title="Hello, Python!",
    topic="Python",
    difficulty=LevelDifficulty.BEGINNER,
    learning_outcomes=["Write your first program"]
)

curriculum.add_lesson("python_basics", lesson)
curriculum.export_curriculum("curriculum.json")
```

### 3. **ProgressTracker**
Track student achievement and learning:
- Record lesson completion
- Track quiz scores
- Monitor time spent
- Record challenge completion
- Award badges
- Export progress reports

```python
from jupyter_learning_system import ProgressTracker

tracker = ProgressTracker("Emma")
tracker.start_lesson("python_hello", "Hello, Python!")
tracker.complete_lesson("python_hello", completion_percentage=100, quiz_score=95)
tracker.add_points(100, "Completed lesson")
tracker.award_badge("first_lesson")
tracker.export_progress("emma_progress.json")
```

### 4. **BadgeSystem**
Gamification through achievements:
- Pre-defined badges (First Steps, Code Warrior, Quiz Master, etc.)
- Custom badge creation
- Badge points and descriptions
- Motivation through achievement tracking

```python
from jupyter_learning_system import BadgeSystem

badge_system = BadgeSystem()
first_lesson_badge = badge_system.get_badge("first_lesson")
print(badge_system.get_badge_display(first_lesson_badge))
# Output: 🎓 First Steps - Complete your first lesson! (+50 points)
```

## Pre-built Lesson Templates

The system comes with templates for fundamental programming concepts:

- **Python Basics**: Hello World, Variables, Data Types, Strings
- **Control Flow**: If/Else, Loops, Functions
- **Data Structures**: Lists, Dictionaries, Tuples
- **JSON/JSON-L**: Parsing, Creating, Working with APIs
- **Linux Basics**: Commands, File System, Permissions
- **Command Prompt**: Navigation, File Operations, System Info

More templates coming soon!

## Curriculum Examples

### Suggested Learning Paths

#### 🐣 **Beginner (Ages 8-10)**
1. Python Basics
2. Variables & Data Types
3. Print & Input
4. Simple Loops
5. Basic Functions

#### 🦅 **Intermediate (Ages 10-12)**
1. Advanced Python Concepts
2. Lists and Dictionaries
3. JSON Files
4. API Basics
5. Linux Introduction

#### 🚀 **Advanced (Ages 12+)**
1. Object-Oriented Programming
2. File I/O
3. Web Scraping Basics
4. Advanced Linux
5. Database Basics

## Customization

### Create Custom Lessons

```python
from jupyter_learning_system import NotebookGenerator

# Create from scratch
notebook = NotebookGenerator("Custom Lesson", author="You")
notebook.set_title_and_intro("Topic", "Introduction text")

# Add sections
notebook.add_markdown_cell("## Section 1")
notebook.add_code_cell("# Your code here")
notebook.add_visual_exercise("Draw ASCII Art", "Create your design")
notebook.add_fun_fact("Interesting Python fact here!")

# Save
notebook.save("custom_lesson.ipynb")
```

### Create Custom Badges

```python
from jupyter_learning_system import BadgeSystem, BadgeType

badge_system = BadgeSystem()
custom_badge = badge_system.create_custom_badge(
    badge_id="my_achievement",
    name="Math Wizard",
    description="Complete 10 math problems",
    badge_type=BadgeType.COMPLETION,
    icon_emoji="🧙‍♂️",
    points=500,
    criteria="Complete 10 math-related lessons"
)
```

## Testing

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=jupyter_learning_system tests/

# Lint code
flake8 jupyter_learning_system/

# Type checking
mypy jupyter_learning_system/
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements 🔮

- [ ] Web UI for generating lessons
- [ ] Interactive notebook preview
- [ ] Lesson template marketplace
- [ ] Real-time collaboration features
- [ ] Integration with learning management systems (LMS)
- [ ] Support for more languages (JavaScript, Java, etc.)
- [ ] Video integration
- [ ] Automated assessment and grading
- [ ] Parent dashboard for progress monitoring

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support & Questions

- 📧 Email: support@proiso.org
- 💬 Discord: [Join Community](https://discord.gg/)
- 📖 Documentation: [Read Docs](https://jupyter-learning-system.readthedocs.io/)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/jupyter-learning-system/issues)

---

Made with ❤️ for educators and young learners everywhere!
