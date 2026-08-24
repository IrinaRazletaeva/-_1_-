class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finish_course = []
        self.course_in_prigress = []
        self.grades = {}


def add_course(self, course_name):
        self.finish_course.append(course_name)

class Mentor :
       def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.course_in_prigress:
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
    else:
        return 'Ошибка'

class Lecturer (Mentor) :
    def __init__(self, name, surname):
        super().__init__(name, surname)



class Reviewer (Mentor) :
    def __init__(self, name, surname):
        super().__init__(name, surname)


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor))
print(isinstance(reviewer, Mentor))
print(lecturer.courses_attached)
print(reviewer.courses_attached)

best_student = Student ('Roy' , 'Eman' , 'your_gender')
best_student.finish_course += ['Git']
best_student.course_in_prigress += ['Phyton']
best_student.grades ['Git'] = [10, 10, 10, 10, 10]
best_student.grades ['Phyton'] = [10, 10]

print (best_student.finish_course)
print(best_student.course_in_prigress)
print(best_student.grades)

cool_mentor = Mentor ('Some', 'Buddy')
cool_mentor.courses_attached += ['Phyton']

cool_mentor.rate_hw (best_student, 'Phyton', 10)
cool_mentor.courses_attached += ['Phyton']

cool_mentor.rate_hw (best_student, 'Phyton', 10)
cool_mentor.rate_hw (best_student, 'Phyton', 10)
cool_mentor.rate_hw (best_student, 'Phyton', 10)

print (best_student.grades)








