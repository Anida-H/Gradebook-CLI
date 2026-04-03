import argparse

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa,
)


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_student_parser = subparsers.add_parser("add-student")
    add_student_parser.add_argument("--name", required=True)

    add_course_parser = subparsers.add_parser("add-course")
    add_course_parser.add_argument("--code", required=True)
    add_course_parser.add_argument("--title", required=True)

    enroll_parser = subparsers.add_parser("enroll")
    enroll_parser.add_argument("--student-id", type=int, required=True)
    enroll_parser.add_argument("--course", required=True)

    add_grade_parser = subparsers.add_parser("add-grade")
    add_grade_parser.add_argument("--student-id", type=int, required=True)
    add_grade_parser.add_argument("--course", required=True)
    add_grade_parser.add_argument("--grade",  required=True)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("entity", choices=["students", "courses", "enrollments"])
    list_parser.add_argument("--sort", required=False)

    avg_parser = subparsers.add_parser("avg")
    avg_parser.add_argument("--student-id", type=int, required=True)
    avg_parser.add_argument("--course", required=True)

    gpa_parser = subparsers.add_parser("gpa")
    gpa_parser.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            student_id = add_student(args.name)
            print(f"Student added successfully with ID {student_id}")

        elif args.command == "add-course":
            add_course(args.code, args.title)
            print("Course added successfully.")

        elif args.command == "enroll":
            enroll(args.student_id, args.course)
            print("Enrollment completed successfully.")

        elif args.command == "add-grade":
            add_grade(args.student_id, args.course, args.grade)
            print("Grade added successfully.")

        elif args.command == "list":
            if args.entity == "students":
                sort_by = args.sort if args.sort else "name"
                students = list_students(sort_by)
                for student in students:
                    print(student)

            elif args.entity == "courses":
                sort_by = args.sort if args.sort else "code"
                courses = list_courses(sort_by)
                for course in courses:
                    print(course)

            elif args.entity == "enrollments":
                enrollments_data = list_enrollments()
                for enrollment_item in enrollments_data:
                    print(enrollment_item)

        elif args.command == "avg":
            average = compute_average(args.student_id, args.course)
            print(f"Average: {average:.2f}")

        elif args.command == "gpa":
            gpa_value = compute_gpa(args.student_id)
            print(f"GPA: {gpa_value:.2f}")

        else:
            parser.print_help()

    except ValueError as error:
        print(f"Error: {error}")
    except KeyError:
        print("Error: Invalid sort field.")


if __name__ == "__main__":
    main()