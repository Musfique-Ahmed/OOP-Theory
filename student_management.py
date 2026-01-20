"""
Student Academic Record Management System
Question 1: Basic Student Academic Record Management
"""


class Course:
    """Course class with private attributes for name and credit"""
    
    def __init__(self, name, credit):
        self.__name = name
        self.__credit = credit
    
    def get_name(self):
        """Getter method for course name"""
        return self.__name
    
    def get_credit(self):
        """Getter method for course credit"""
        return self.__credit
    
    def __str__(self):
        return f"{self.__name} ({self.__credit} credits)"
    
    def __eq__(self, other):
        """Check if two courses are equal based on name"""
        if isinstance(other, Course):
            return self.__name == other.__name
        return False


class Student:
    """Student class with private attributes and encapsulation"""
    
    # Private class-level counters for each department
    __cse_count = 0
    __ds_count = 0
    
    def __init__(self, name, department):
        """Initialize a student with name and department"""
        self.__name = name
        self.__department = department
        self.__current_courses = []
        self.__completed_courses = {}  # {course_name: (course, gpa)}
        self.__cgpa = 0.0
        
        # Generate unique ID based on department
        if department == 'CSE':
            Student.__cse_count += 1
            self.__id = f"011{Student.__cse_count:03d}"
        elif department == 'DS':
            Student.__ds_count += 1
            self.__id = f"015{Student.__ds_count:03d}"
        else:
            raise ValueError("Department must be 'CSE' or 'DS'")
    
    # Getter methods
    def get_name(self):
        """Getter method for student name"""
        return self.__name
    
    def get_department(self):
        """Getter method for department"""
        return self.__department
    
    def get_id(self):
        """Getter method for student ID"""
        return self.__id
    
    def get_current_courses(self):
        """Getter method for current courses"""
        return self.__current_courses.copy()
    
    def get_completed_courses(self):
        """Getter method for completed courses"""
        return self.__completed_courses.copy()
    
    def get_cgpa(self):
        """Getter method for CGPA"""
        return self.__cgpa
    
    @classmethod
    def get_cse_count(cls):
        """Class method to get the number of CSE students"""
        return cls.__cse_count
    
    @classmethod
    def get_ds_count(cls):
        """Class method to get the number of DS students"""
        return cls.__ds_count
    
    def add_course(self, course):
        """
        Adds a course object to the list of current courses
        Prevents duplicates
        """
        if not isinstance(course, Course):
            print("Error: Invalid course object")
            return False
        
        # Check if course already exists in current courses
        if course in self.__current_courses:
            print(f"Error: {course.get_name()} is already in current courses")
            return False
        
        # Check if course already completed
        if course.get_name() in self.__completed_courses:
            print(f"Error: {course.get_name()} has already been completed")
            return False
        
        self.__current_courses.append(course)
        print(f"Course {course.get_name()} added successfully for {self.__name}")
        return True
    
    def add_grade(self, course, gpa):
        """
        Adds grade for a course and updates CGPA
        Course must be in current courses
        GPA must be between 0.0 and 4.0
        """
        # Check if GPA is valid
        if not (0.0 <= gpa <= 4.0):
            print("Error: GPA must be between 0.0 and 4.0")
            return False
        
        # Check if course is in current courses
        if course not in self.__current_courses:
            print(f"Error: {course.get_name()} is not in current courses")
            return False
        
        # Remove course from current courses
        self.__current_courses.remove(course)
        
        # Add to completed courses
        self.__completed_courses[course.get_name()] = (course, gpa)
        
        # Update CGPA using credit-weighted formula
        self.__update_cgpa()
        
        print(f"Grade {gpa} added for {course.get_name()}. Updated CGPA: {self.__cgpa:.2f}")
        return True
    
    def __update_cgpa(self):
        """Private method to update CGPA using credit-weighted formula"""
        total_credits = 0
        weighted_sum = 0
        
        for course_name, (course, gpa) in self.__completed_courses.items():
            credit = course.get_credit()
            total_credits += credit
            weighted_sum += credit * gpa
        
        if total_credits > 0:
            self.__cgpa = weighted_sum / total_credits
        else:
            self.__cgpa = 0.0
    
    def display_info(self):
        """Display student information"""
        print(f"\n{'='*50}")
        print(f"Student ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"CGPA: {self.__cgpa:.2f}")
        
        print(f"\nCurrent Courses ({len(self.__current_courses)}):")
        for course in self.__current_courses:
            print(f"  - {course}")
        
        print(f"\nCompleted Courses ({len(self.__completed_courses)}):")
        for course_name, (course, gpa) in self.__completed_courses.items():
            print(f"  - {course}: GPA {gpa:.2f}")
        print(f"{'='*50}\n")


# Demonstration code
if __name__ == "__main__":
    print("=== Student Academic Record Management System ===\n")
    
    # Create courses
    course1 = Course("Data Structures", 3)
    course2 = Course("Object Oriented Programming", 3)
    course3 = Course("Database Systems", 3)
    course4 = Course("Machine Learning", 3)
    course5 = Course("Web Development", 2)
    
    # Create students
    student1 = Student("Alice", "CSE")
    student2 = Student("Bob", "DS")
    student3 = Student("Charlie", "CSE")
    student4 = Student("Diana", "DS")
    
    print(f"Total CSE Students: {Student.get_cse_count()}")
    print(f"Total DS Students: {Student.get_ds_count()}\n")
    
    # Add courses to student1
    print("--- Adding courses to Alice ---")
    student1.add_course(course1)
    student1.add_course(course2)
    student1.add_course(course3)
    
    # Try to add duplicate course
    student1.add_course(course1)  # Should fail
    
    print("\n--- Adding grades for Alice ---")
    student1.add_grade(course1, 3.7)
    student1.add_grade(course2, 4.0)
    student1.add_grade(course3, 3.5)
    
    # Try to add grade for course not enrolled
    student1.add_grade(course4, 3.8)  # Should fail
    
    # Display student info
    student1.display_info()
    
    # Add courses to student2
    print("--- Adding courses to Bob ---")
    student2.add_course(course4)
    student2.add_course(course5)
    student2.add_grade(course4, 3.9)
    student2.add_grade(course5, 3.6)
    
    student2.display_info()
    
    # Test invalid GPA
    print("--- Testing invalid operations ---")
    student3.add_course(course1)
    student3.add_grade(course1, 5.0)  # Should fail - GPA > 4.0
    student3.add_grade(course1, 3.8)  # Should succeed
    
    student3.display_info()
    
    print(f"\nFinal Count - CSE: {Student.get_cse_count()}, DS: {Student.get_ds_count()}")
