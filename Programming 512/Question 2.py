class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def __str__(self):
        return f"{self.name}\nAge: {self.age}\nID: {self.id}"
    
class Student(Person):
    def __init__(self, name, age, id, major):
        super().__init__(name, age, id)
        self.major = major
        self.enrolled_courses = []
        self.course_options = ["HCIT", "BSCIT", "BCOM", "DIT", "BA", "DBA"]
        def enroll(self, course):
            capacity = len(self.enrolled_courses) < 1
            if capacity:
                for counter, course in enumerate(self.course_options):
                    print(f"{counter + 1}. {course}")
                course_picked = input("Pick a course (1 - 6): ")
                if course_picked == "1":
                    self.enrolled_courses.append(self.course_options[0])
                    for course in self.enrolled_courses:
                        print("Successfully enrolled in {course}.")
                elif course_picked == "2":
                    self.enrolled_courses.append(self.course_options[1])
                    for course in self.enrolled_courses:
                        print("Successfully enrolled in {course}.")
                elif course_picked == "3":
                    self.enrolled_courses.append(self.course_options[2])
                    for course in self.enrolled_courses:
                        print("Successfully enrolled in {course}.")
                elif course_picked == "4":
                    self.enrolled_courses.append(self.course_options[3])
                    for course in self.enrolled_courses:
                        print("Successfully enrolled in {course}.")
                elif course_picked == "5":
                    self.enrolled_courses.append(self.course_options[4])
                    for course in self.enrolled_courses:
                        print("Successfully enrolled in {course}.")
                elif course_picked == "6":
                    self.enrolled_courses.append(self.course_options[5])
                    for course in self.enrolled_courses:
                        print("Successfully enrolled in {course}.")
            else:
                return "Already enrolled in a course."