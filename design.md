# System Design

## 1. Functional Modules

The Study Hours Tracker consists of the following major functional modules:

### 1.1 Study Session Module

Collects the student's name, study hours, study goal, subject, and topic.

### 1.2 Goal Tracking Module

Calculates the percentage of the study goal completed and determines whether the goal has been achieved.

### 1.3 Checklist Module

Collects a general to-do list and subject-wise study tasks.

### 1.4 Reporting Module

Displays a summary of the student's study session, including study hours, goal, number of sessions, progress, and checklist.

---

# 2. Non-Functional Requirements

## 2.1 Usability

The application should be simple and easy to use. Users interact with the system through clear prompts and receive readable output.

## 2.2 Performance

The application should process user input and calculate study progress quickly without unnecessary processing.

## 2.3 Reliability

The application should correctly calculate study progress and display the corresponding study-goal status based on the entered values.

## 2.4 Maintainability

The project is divided into separate Python modules so that individual functionality can be modified or extended without unnecessarily changing the entire application.

---



# 3. Workflow

```text
Start
  |
  v
Enter Student Details
  |
  v
Enter Study Hours and Goal
  |
  v
Enter Subject and Topic
  |
  v
Enter To-Do List
  |
  v
Enter Subject-wise Checklist
  |
  v
Enter Completed Sessions
  |
  v
Calculate Goal Progress
  |
  v
Check Goal Status
  |
  v
Generate Study Report
  |
  v
End
```

---

# 4. Use Case Description

## Primary Actor

Student

## Main Use Cases

* Enter study details
* Set study goal
* Enter study hours
* Add study topic
* Add to-do tasks
* Add subject-wise checklist
* Enter completed sessions
* View goal progress
* View study summary

---

# 5. Input and Output

## Inputs

The application accepts:

* Student name
* Study hours
* Study goal
* Subject
* Topic
* General to-do list
* Subject-wise checklist
* Number of completed study sessions

## Outputs

The application produces:

* Study-goal status
* Remaining study hours
* Goal progress percentage
* Study-session summary
* General to-do list
* Subject-wise checklist

---

# 6. Future Design Improvements

Future versions of the application could include:

* Permanent storage of study sessions
* Date and time tracking
* Graphical progress charts
* Database integration
* Graphical user interface
* Multiple student profiles
* Long-term study analytics
