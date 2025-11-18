"""
NotebookGenerator: Core module for programmatically generating Jupyter notebooks.
Converts lesson templates into interactive, kid-friendly notebooks with code cells,
quizzes, and visual elements.
"""

import json
import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path


class NotebookGenerator:
    \"\"\"Generate Jupyter notebooks from lesson templates and blocks.\"\"\"
    
    NOTEBOOK_VERSION = 4
    MIMETYPE_CODE = "code"
    MIMETYPE_MARKDOWN = "markdown"
    MIMETYPE_RAW = "raw"
    
    def __init__(self, title: str, description: str = "", author: str = "Learning System"):
        \"\"\"Initialize notebook generator with metadata.\"\"\"
        self.title = title
        self.description = description
        self.author = author
        self.cells = []
        self.metadata = {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.9.0"
            }
        }
    
    def add_markdown_cell(self, content: str, tags: Optional[List[str]] = None) -> 'NotebookGenerator':
        \"\"\"Add a markdown cell to the notebook.\"\"\"
        cell = self._create_cell(
            cell_type="markdown",
            source=content,
            tags=tags or []
        )
        self.cells.append(cell)
        return self
    
    def add_code_cell(self, code: str, tags: Optional[List[str]] = None, 
                     execution_count: Optional[int] = None) -> 'NotebookGenerator':
        \"\"\"Add a Python code cell to the notebook.\"\"\"
        cell = self._create_cell(
            cell_type="code",
            source=code,
            tags=tags or [],
            execution_count=execution_count
        )
        self.cells.append(cell)
        return self
    
    def add_quiz_cell(self, question: str, options: List[str], correct_index: int,
                     explanation: str = "") -> 'NotebookGenerator':
        \"\"\"Add an interactive quiz cell (markdown with code hook).\"\"\"
        quiz_content = f\"\"\"## 🎯 Quiz Question

**{question}**

\"\"\"
        for i, option in enumerate(options):
            quiz_content += f\"- {chr(65 + i)}) {option}\\n\"
        
        self.add_markdown_cell(quiz_content, tags=["quiz"])
        
        if explanation:
            self.add_markdown_cell(f\"**Answer Explanation:**\\n{explanation}\", tags=[\"quiz-answer\"])
        
        return self
    
    def add_challenge_cell(self, challenge_title: str, description: str,
                          starter_code: str = "", hints: Optional[List[str]] = None) -> 'NotebookGenerator':
        \"\"\"Add a code challenge cell with hints.\"\"\"
        content = f\"\"\"## 🚀 Challenge: {challenge_title}

{description}

\"\"\"
        if hints:
            content += \"\\n**Hints:**\\n\"
            for i, hint in enumerate(hints, 1):
                content += f\"- Hint {i}: {hint}\\n\"
        
        self.add_markdown_cell(content, tags=["challenge"])
        
        if starter_code:
            self.add_code_cell(starter_code, tags=["challenge-code"])
        else:
            self.add_code_cell("# Write your code here", tags=["challenge-code"])
        
        return self
    
    def add_visual_exercise(self, title: str, description: str,
                           visual_type: str = "ascii_art") -> 'NotebookGenerator':
        \"\"\"Add a visual/interactive exercise cell.\"\"\"
        content = f\"\"\"## 🎨 Visual Exercise: {title}

{description}

\"\"\"
        self.add_markdown_cell(content, tags=["visual-exercise"])
        
        if visual_type == "ascii_art":
            example = '''
# Example ASCII Art - Modify this!
print(\"\"\"
    ~~~~ Fun Program ~~~~
    🎉 Learning is Fun! 🎉
\"\"\")
'''
            self.add_code_cell(example, tags=["visual-code"])
        
        return self
    
    def add_fun_fact(self, fact: str) -> 'NotebookGenerator':
        \"\"\"Add a fun fact or learning nugget.\"\"\"
        content = f\"\"\"### 💡 Did You Know?

{fact}
\"\"\"
        self.add_markdown_cell(content, tags=["fun-fact"])
        return self
    
    def set_title_and_intro(self, title: str, introduction: str) -> 'NotebookGenerator':
        \"\"\"Add a title and introduction to the notebook.\"\"\"
        # Title
        self.add_markdown_cell(f\"# {title}\")
        
        # Metadata
        meta = f\"\"\"
**Author:** {self.author}  
**Created:** {datetime.now().strftime('%B %d, %Y')}  
**Topic:** {self.title}
\"\"\"
        self.add_markdown_cell(meta)
        
        # Introduction
        self.add_markdown_cell(introduction)
        
        return self
    
    def generate(self) -> Dict[str, Any]:
        \"\"\"Generate the complete notebook as a dictionary.\"\"\"
        notebook = {
            "cells": self.cells,
            "metadata": self.metadata,
            "nbformat": self.NOTEBOOK_VERSION,
            "nbformat_minor": 4
        }
        return notebook
    
    def save(self, filepath: str) -> str:
        \"\"\"Save the notebook to a file.\"\"\"
        notebook = self.generate()
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2)
        
        return str(path.absolute())
    
    def to_json(self) -> str:
        \"\"\"Export notebook as JSON string.\"\"\"
        return json.dumps(self.generate(), indent=2)
    
    @staticmethod
    def _create_cell(cell_type: str, source: str, tags: List[str] = None,
                    execution_count: Optional[int] = None) -> Dict[str, Any]:
        \"\"\"Create a cell structure compatible with Jupyter notebook format.\"\"\"
        cell = {
            "cell_type": cell_type,
            "metadata": {
                "tags": tags or []
            },
            "source": source.split('\\n') if isinstance(source, str) else source,
        }
        
        if cell_type == "code":
            cell["execution_count"] = execution_count
            cell["outputs"] = []
        
        return cell
