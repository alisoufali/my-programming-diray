# my_programming_diary

A simple cli-based program with SQLite database about my diary on programming

- [my_programming_diary](#my_programming_diary)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [How to Run](#how-to-run)

## Requirements

This project has the following dependencies:

```txt
python>=3.8
PyPika==0.48.9
```

## Installation

To be able to use and run this project, first we need to make a virtual environment, activate it and install depdendencies

```bash
# Creating virtual environment (venv)
python -m venv .venv

# Sourcing the created venv
source .venv/bin/activate      # If Running on Linux/MacOS
source .venv/Scripts/activate  # If Running on Windows

# Updating pip package manager for venv
python -m pip install --upgrade pip

# Installing dependencies
pip install -r requirements.txt
```

## How to Run

To run the application just execute the following:

```bash
python app.py
```
