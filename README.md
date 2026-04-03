# Gradebook CLI

A simple Python command-line application for managing students, courses, enrollments, and grades.

## Project Structure


gradebook/

gradebook/
init.py
models.py
storage.py
service.py
data/
gradebook.json
logs/
app.log
scripts/
seed.py
tests/
test_service.py
main.py
README.md

## Setup

### 1. Create a virtual environment

```bash```
python -m venv venv

2. Activate the virtual environment

On Windows:

```bash```
venv\Scripts\activate

On macOS/Linux:

```bash```
source venv/bin/activate

How to Run the Application

Run commands from the project root folder.

Add a student
```bash```
python main.py add-student --name "Zack"

Add a course
```bash```
python main.py add-course --code CS103 --title "Electronics"

Enroll a student in a course
```bash```
python main.py enroll --student-id 1 --course CS103

Add a grade
```bash```
python main.py add-grade --student-id 1 --course CS103 --grade 95

List students
```bash```
python main.py list students

List courses
```bash```
python main.py list courses

List enrollments
```bash```
python main.py list enrollments

Compute average for a course
```bash```
python main.py avg --student-id 1 --course CS101

Compute GPA for a student
```bash```
python main.py gpa --student-id 1

Sample Data

To populate the project with sample data, run:
```bash```
python -m scripts.seed

This will save sample data into:
data/gradebook.json
Run Tests
```bash```
python -m unittest discover -s tests
Logging

The application writes log messages to:

logs/app.log

It logs:
successful load/save operations
JSON errors
file write errors
Design Decisions & Limitations
Design Decisions
JSON was used for persistence because it is simple and easy to inspect.

The project is organized into modules:
models.py for data models
storage.py for file handling
service.py for business logic
main.py for the command-line interface
Helper validation such as parse_grade() is used to keep validation logic clean.
Logging was added to make the application easier to debug.

Limitations
Data is stored in a local JSON file, not in a database.
GPA is calculated as the simple mean of course averages.
The project does not support deleting or updating students/courses.
Sorting options are limited to existing fields.
Tests currently use the same JSON file used by the application.
