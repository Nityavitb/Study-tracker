# Study Hours Tracker

## Overview

Study Hours Tracker is a Python-based productivity application designed to help students record and monitor their study sessions.

The application allows users to enter their study details, set a study goal, maintain a subject-wise to-do checklist, calculate their study progress, and generate a study session summary.

The project demonstrates the practical use of Python programming concepts such as user input, variables, conditional statements, dictionaries, loops, functions, modules, calculations, and basic testing.

---

## Features

* Student name input
* Study hours tracking
* Study goal setting
* Subject and topic tracking
* General study-session to-do list
* Subject-wise checklist
* Study session count
* Study goal achievement check
* Remaining study-hours calculation
* Goal progress percentage
* Study session summary report
* Modular Python implementation
* Basic automated testing

---

## Technologies Used

* Python 3
* Visual Studio Code
* Git
* GitHub
* Pytest for testing

---

## Project Structure

```text
Study-Hours-Tracker/
│
├── main.py
├── study_tracker.py
├── goals.py
├── checklist.py
├── reports.py
├── README.md
│
└── tests/
    └── test_tracker.py
```

### File Description

| File               | Purpose                                              |
| ------------------ | ---------------------------------------------------- |
| `main.py`          | Main program that connects all modules               |
| `study_tracker.py` | Collects student and study-session information       |
| `goals.py`         | Calculates study progress and checks study goals     |
| `checklist.py`     | Handles the general and subject-wise to-do lists     |
| `reports.py`       | Generates the final study-session report             |
| `test_tracker.py`  | Contains basic tests for study-progress calculations |

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone <link>
```

### 2. Open the project folder

```bash
cd Study-Hours-Tracker
```

### 3. Run the application

```bash
python main.py
```

The program will ask the user for study information and display a study progress report.

---

## Testing

The project includes basic tests for the study-progress calculation.

To run the tests:

```bash
python -m pytest
```

The tests verify calculations such as:

* 9 hours studied out of a 12-hour goal → 75% progress
* 12 hours studied out of a 12-hour goal → 100% progress
* 5 hours studied out of a 10-hour goal → 50% progress

---

## Example

A sample session may contain:

```text
Student Name: Nitya
Subject Studied: Mathematics
Topic Studied: Calculus
Hours Studied: 9
Study Goal: 12
Total Sessions Completed: 2
Goal Progress: 75.0 %
Status: Goal In Progress
```

The application also displays the user's general and subject-wise to-do lists.

---

## Future Enhancements

Possible future improvements include:

* Saving study sessions permanently
* Adding dates and timestamps
* Tracking progress over multiple days
* Graphical progress visualization
* A graphical user interface
* User login and multiple student profiles
* Database integration
* More detailed study analytics

---

## Project Purpose

The purpose of this project is to provide students with a simple tool for monitoring study time and goals while demonstrating practical Python programming and modular software development concepts.

---

## Author

**Nitya Srivastava**

**Project:** Study Hours Tracker
**Course:** VITyarthi
