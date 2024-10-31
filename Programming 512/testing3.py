class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID: {self.id}\n"


class Student(Person):
    def __init__(self, name, age, id, major):
        super().__init__(name, age, id)
        self.major = major
        self.enrolled_courses = []

    def enroll(self, course):
        if course.add_student(self):
            self.enrolled_courses.append(course)
            print(f"{self.name} has enrolled in {course.name}.")
        else:
            print(f"{course.name} is full. {self.name} could not enroll.")

    def drop(self, course):
        if course in self.enrolled_courses:
            course.remove_student(self)
            self.enrolled_courses.remove(course)
            print(f"{self.name} has dropped {course.name}.")
        else:
            print(f"{self.name} is not enrolled in {course.name}.")


class Professor(Person):
    def __init__(self, name, age, id, department):
        super().__init__(name, age, id)
        self.department = department
        self.courses_teaching = []

    def assign_course(self, course):
        self.courses_teaching.append(course)
        course.professor = self
        print(f"{self.name} is now teaching {course.name}.")


class Course:
    def __init__(self, course_code, name, max_capacity):
        self.course_code = course_code
        self.name = name
        self.max_capacity = max_capacity
        self.professor = None
        self.enrolled_students = []

    def __str__(self):
        return f"{self.name} ({self.course_code}), Capacity: {len(self.enrolled_students)}/{self.max_capacity}"

    def add_student(self, student):
        if len(self.enrolled_students) < self.max_capacity:
            self.enrolled_students.append(student)
            return True
        return False

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"{student.name} has been removed from {self.name}.")
        else:
            print(f"{student.name} is not enrolled in {self.name}.")


class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        self.professors = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def get_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        return None

university = University("University")

course1 = Course("512", "Mathematics", 5)
course2 = Course("622", "Accounting", 5)

university.add_course(course1)
university.add_course(course2)

student1 = Student("Thapelo", 20, "402165574", "BSCIT")
student2 = Student("Pete", 21, "456120154", "BCOM")
student3 = Student("George", 22, "411523369", "BCOM")

university.add_student(student1)
university.add_student(student2)
university.add_student(student3)

professor1 = Professor("Dr. Smith", 45, "RoyalG", "Computer Science")
professor2 = Professor("Dr. Johnson", 50, "SilasT", "Mathematics")

university.add_professor(professor1)
university.add_professor(professor2)

professor1.assign_course(course1)
professor2.assign_course(course2)


student1.enroll(course1)
student2.enroll(course2)
student3.enroll(course2)
student3.enroll(course1)   


student2.drop(course2)

print("\nCourses:")
for course in university.courses:
    print(course)

print("\nStudents:")
for student in university.students:
    print(student)

print("\nProfessors:")
for professor in university.professors:
    print(professor)
