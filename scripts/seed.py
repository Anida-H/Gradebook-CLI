# This script creates sample data for testing the gradebook.

from gradebook.storage import save_data


sample_data = {
    "students": [
        {"id": 1, "name": "Anida"},
        {"id": 2, "name": "Artina"},
        {"id": 3, "name": "Sara"}
    ],
    "courses": [
        {"code": "CS101", "title": "Intro to CS"},
        {"code": "MATH201", "title": "Discrete Math"}
    ],
    "enrollments": [
        {"student_id": 1, "course_code": "CS101", "grades": [90, 95]},
        {"student_id": 1, "course_code": "MATH201", "grades": [85]},
        {"student_id": 2, "course_code": "CS101", "grades": [88, 92]},
        {"student_id": 3, "course_code": "MATH201", "grades": [75, 80]}
    ]
}


if __name__ == "__main__":
    save_data(sample_data)
    print("Sample data has been saved to data/gradebook.json")