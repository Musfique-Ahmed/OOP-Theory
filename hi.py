class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits

    def display_info(self):
        print(f"Course Name: {self.course_name}, Credits: {self.credits}")



class Student:
    current_id = 0

    def __init__(self, name):
        self.name = name
        Student.current_id += 1 # Increment student ID: Student.current_id = Student.current_id + 1
        self.student_id = Student.current_id
        self.courses = []
        self.results = {}

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course.course_name}")


    def add_result(self, course, grade):
        if course in self.courses:
            self.results[course.course_name] = grade
            print(f"Added result for {self.name}: {course.course_name} - {grade}")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")

    def display_info(self):
        print(f"Student Name: {self.name}, ID: {self.student_id}")
        print("Enrolled Courses:")
        for course in self.courses:
            print(f"- {course.course_name}")
        print("Results:")
        for course_name, grade in self.results.items():
            print(f"- {course_name}: {grade}")


# Example usage

bangla = Course("Bangla", 3)
bangla.display_info()

english = Course("English", 3)
english.display_info()


student1 = Student("Alice")
student1.enroll(bangla)
student1.enroll(english)
# student1.enroll("Math")  # This will not work as intended since "Math" is not a Course object
student1.enroll(Course("Math", 4))  # Correct way to enroll in Math

print("\n--- Results ---\n")

student1.add_result(bangla, "A")
student1.add_result(english, "B+")
student1.add_result(Course("Math", 4), "A")  # This will not work as intended since Math is not enrolled


print("\n--- Student Info ---\n")
student1.display_info()



student2 = Student("Bob")
student2.enroll(bangla)
student2.add_result(bangla, "A-")
print("\n--- Student 2 Info ---\n")
student2.display_info()