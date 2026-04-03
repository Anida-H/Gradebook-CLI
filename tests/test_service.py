import unittest

from gradebook.storage import save_data
from gradebook.service import add_student, add_grade, compute_average


class TestGradebookService(unittest.TestCase):
    def setUp(self):
        """Reset test data before each test."""
        save_data({
            "students": [],
            "courses": [],
            "enrollments": []
        })

    def test_add_student(self):
        """Test that a student is added and gets ID 1."""
        student_id = add_student("Anida")
        self.assertEqual(student_id, 1)

    def test_add_grade(self):
        """Test adding a grade to an existing enrollment."""
        save_data({
            "students": [{"id": 1, "name": "Anida"}],
            "courses": [{"code": "CS101", "title": "Intro to CS"}],
            "enrollments": [{"student_id": 1, "course_code": "CS101", "grades": []}]
        })

        add_grade(1, "CS101", 95)
        average = compute_average(1, "CS101")
        self.assertEqual(average, 95.0)

    def test_compute_average(self):
        """Test average calculation for multiple grades."""
        save_data({
            "students": [{"id": 1, "name": "Anida"}],
            "courses": [{"code": "CS101", "title": "Intro to CS"}],
            "enrollments": [{"student_id": 1, "course_code": "CS101", "grades": [90, 100]}]
        })

        average = compute_average(1, "CS101")
        self.assertEqual(average, 95.0)

    def test_add_grade_fails_for_missing_enrollment(self):
        """Test that adding a grade fails if enrollment does not exist."""
        save_data({
            "students": [{"id": 1, "name": "Anida"}],
            "courses": [{"code": "CS101", "title": "Intro to CS"}],
            "enrollments": []
        })

        with self.assertRaises(ValueError):
            add_grade(1, "CS101", 90)


if __name__ == "__main__":
    unittest.main()