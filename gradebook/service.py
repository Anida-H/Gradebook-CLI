#service.py will be the layer that: 
# reads data from storage.py, makes changes,stores data back,calculates average and GPA,returns sorted lists
from .storage import load_data, save_data

# This function adds a new student to the gradebook.
# It generates a new unique ID, saves the student, and returns the ID.
def add_student(name):
    data = load_data()

    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    if data["students"]:
        new_id = max(student["id"] for student in data["students"]) + 1
    else:
        new_id = 1

    new_student = {
        "id": new_id,
        "name": name
    }

    data["students"].append(new_student)
    save_data(data)

    return new_id


# This function adds a new course to the gradebook.
# It checks that the course code and title are not empty
# and prevents duplicate course codes.
def add_course(code, title):
    data = load_data()

    if not code.strip():
        raise ValueError("Course code cannot be empty.")
    if not title.strip():
        raise ValueError("Course title cannot be empty.")

    for course in data["courses"]:
        if course["code"] == code:
            raise ValueError("Course code already exists.")

    new_course = {
        "code": code,
        "title": title
    }

    data["courses"].append(new_course)
    save_data(data)

# This function enrolls a student in a course.
# It checks whether the student and course exist
# and prevents duplicate enrollments.
def enroll(student_id, course_code):
    data = load_data()

    student_exists = any(student["id"] == student_id for student in data["students"])
    if not student_exists:
        raise ValueError("Student not found.")

    course_exists = any(course["code"] == course_code for course in data["courses"])
    if not course_exists:
        raise ValueError("Course not found.")

    already_enrolled = any(
        enrollment["student_id"] == student_id and enrollment["course_code"] == course_code
        for enrollment in data["enrollments"]
    )
    if already_enrolled:
        raise ValueError("Student is already enrolled in this course.")

    new_enrollment = {
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    }

    data["enrollments"].append(new_enrollment)
    save_data(data)

# This helper function validates and converts a grade input.
# It makes sure the grade is numeric and between 0 and 100.
def parse_grade(grade):
    try:
        grade = float(grade)
    except ValueError:
        raise ValueError("Grade must be a number.")

    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100.")

    return grade

# This function adds a grade to an existing enrollment.
def add_grade(student_id, course_code, grade):
    data = load_data()

    grade = parse_grade(grade)

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            enrollment["grades"].append(grade)
            save_data(data)
            return

    raise ValueError("Enrollment not found.")

# This function returns all students sorted by name.
def list_students(sort_by="name"):
    data = load_data()
    return sorted(data["students"], key=lambda student: student[sort_by])
# This function returns all courses sorted by course code.
def list_courses(sort_by="code"):
    data = load_data()
    return sorted(data["courses"], key=lambda course: course[sort_by])

# This function returns all enrollments sorted by student ID and course code.
def list_enrollments():
    data = load_data()
    return sorted(
        data["enrollments"],
        key=lambda enrollment: (enrollment["student_id"], enrollment["course_code"])
    )

# This function computes the average grade for one student's course enrollment.
def compute_average(student_id, course_code):
    data = load_data()

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            grades = enrollment["grades"]

            if not grades:
                raise ValueError("No grades available for this enrollment.")

            return sum(grades) / len(grades)

    raise ValueError("Enrollment not found.")

# This function computes the GPA for a student.
# GPA here is the simple mean of all course averages for that student.
def compute_gpa(student_id):
    data = load_data()

    student_enrollments = [
        enrollment
        for enrollment in data["enrollments"]
        if enrollment["student_id"] == student_id
    ]

    if not student_enrollments:
        raise ValueError("Student has no enrollments.")

    course_averages = []

    for enrollment in student_enrollments:
        grades = enrollment["grades"]
        if grades:
            average = sum(grades) / len(grades)
            course_averages.append(average)

    if not course_averages:
        raise ValueError("Student has no grades.")

    return sum(course_averages) / len(course_averages)

#testing
if __name__ == "__main__":
    print(add_student("Test Student"))

    #run python -m gradebook.service per te shtuar student te ri

#6 Input validation(helper functions)
# This helper function validates and converts a grade input.
# It ensures the grade is numeric and between 0 and 100.
def parse_grade(grade):
    try:
        grade = float(grade)
    except ValueError:
        raise ValueError("Grade must be a number.")

    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100.")

    return grade