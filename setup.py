"""
Setup configuration for jupyter-learning-system package.
"""

from setuptools import setup, find_packages

setup(
    name="jupyter-learning-system",
    version="0.1.0",
    description="Educational Jupyter notebook generation system for children",
    author="Justin Crawford",
    author_email="",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "jupyter>=1.0.0",
        "click>=8.0.0",
        "nbformat>=5.0.0",
    ],
    entry_points={
        "console_scripts": [
            "jupyter-learning=jupyter_learning_system.cli.main:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
