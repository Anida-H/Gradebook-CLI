class Student:
    def __init__(self , student_id , name):
        if not name:
            raise ValueError("Name cannot be empty!")
        self.id = student_id
        self.name = name
    
    def __str__(self):
        return f"Student(id={self.id} , name='{self.name}')"
    

class Course:
    def __init__(self , code , title ):
        if not code or not title:
            raise ValueError("Course fields cannot be empyt!")
        self.code = code
        self.title = title
        
    def __str__(self):
        return f"Course(code='{self.code}', title='{self.title}')"

class Enrollment:
    def __init__(self, student_id , course_code , grades = None):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades else[]

        #isinstance is a built-in function , siintaksa : isinstance(object , (type1,type2))
        for g in self.grades:
            if not isinstance(g, (int, float)) or not (0 <= g <= 100):
                raise ValueError("Grades must be between 0 and 100")
        
    def __str__(self):
        return f"Enrollment(student_id={self.student_id}, course_code='{self.course_code}', grades={self.grades})"
    
#testing
# if __name__ == "__main__":
#     s = Student(1, "Anida")
#     c = Course("CS101", "Intro to CS")
#     e = Enrollment(1, "CS101", [90, 80.5])

#     print(s)
#     print(c)
#     print(e)