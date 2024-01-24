# A class is a blue-print for creating objects.
# In this code implementation of OOP in Python, 
# we shall implement an object-oriented database for the UG Student MIS


# SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = f'{firstName[0]}{lastName}@st.ug.edu'.lower()

    def fullName(self):
        return f' {self.firstName} {self.lastName}'
    
    def intials(self):
        return f'{self.firstName[0]}.{self.lastName[0]}'




# SECTION TWO
# 1. Define a class Student which inherites from the Person class
# 2. Define extra attributes for student, such as hall of residence and courses
# 3. Create a student object from the Student class

class Student(Person):
    def __init__(self,firstName,lastName,age, hall,courses =None):
        super().__init__(firstName,lastName,age)
        self.hall = hall
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self,course_title):
        if course_title not in self.courses:
            self.courses.append(course_title)

    def drop_course(self,course_title):
        if course_title  in self.courses:
            self.courses.remove(course_title)

    def print_all_courses(self):
        print(f' {self.fullName()} has registered {len(self.courses)} courses')
        print('-'*40)
        for courses in self.courses:
            print(courses)

student1 =Student('Alexander','Giffah',21,'Legon hall')
student1.add_course('python')
student1.add_course('Algebra')
student1.add_course('SOM')
student1.drop_course('OOP')
print(student1.print_all_courses())
    






# """
#     4. Write a add_course, drop_course, print_all_courses method to mimic 
#     a real-world use-case of activities of adding a course, 
#     deleting a course and printing registered courses respectively
#     a student will perform on the Student MIS 
  
# Magic Methods
# Overwrite string method 