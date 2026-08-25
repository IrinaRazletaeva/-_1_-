class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def add_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course].append(grade)
            return f"Оценка {grade} за курс {course} выставлена лектору {lecturer.name}"
        return "Ошибка: Не удалось выставить оценку"

    def __str__(self):
        avg_grade = 0
        if self.grades:
            all_grades = []
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'нет'
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'нет'
        return (f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашнее задание: {avg_grade:.1f}\n"
            f"Курсы процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}\n")
            

class Mentor :
       def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


def __str__(self):
    return (f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n")


class Lecturer (Mentor) :
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = 0
        if self.grades:
            all_grades = []
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0


        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}\n")

class Reviewer (Mentor) :
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, courses, grade):
        if isinstance(student, Student) and courses in self.courses_attached and courses in student.courses_in_progress:
            if courses in student.grades:
                student.grades[courses] += [grade]
            else:
                student.grades[courses] = [grade]
            return f"Оценка {grade} за домашнее задание по курсу {courses} выставлена студенту {student.name}"
        return 'Ошибка'


    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")

def average_hw_grade(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if all_grades:
        return round(sum(all_grades) / len(all_grades), 1)
    return 0.0


def average_lecturer_grade(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if all_grades:
        return round(sum(all_grades) / len(all_grades), 1)
    return 0.0

lecturer1 = Lecturer("Игорь", "Иванов")
lecturer1.courses_attached = ["Python", "Java"]

lecturer2 = Lecturer("Иван", "Петров")
lecturer2.courses_attached = ["Python", "C#"]

reviewer1 = Reviewer("Максим", "Федоров")
reviewer1.courses_attached = ["Python", "Java"]

reviewer2 = Reviewer("Ирина", "Антонова")
reviewer2.courses_attached = ["Python", "C#"]

student1 = Student("Валентина", "Алёхина", "Ж")
student1.courses_in_progress = ["Python", "Java"]
student1.finished_courses = ["Git"]

student2 = Student("Алексей", "Соколов", "М")
student2.courses_in_progress = ["Python", "C#"]
student2.finished_courses = ["Git", "HTML"]


print("\n--- Ревьюеры выставляют оценки студентам ---")
print(reviewer1.rate_hw(student1, "Python", 10))
print(reviewer1.rate_hw(student1, "Python", 9))
print(reviewer1.rate_hw(student1, "Java", 8))
print(reviewer2.rate_hw(student2, "Python", 7))
print(reviewer2.rate_hw(student2, "Python", 8))
print(reviewer2.rate_hw(student2, "C#", 9))

# 2. Студенты выставляют оценки лекторам
print("\n--- Студенты выставляют оценки лекторам ---")
print(student1.rate_lecturer(lecturer1, "Python", 10))
print(student1.rate_lecturer(lecturer1, "Python", 9))
print(student1.rate_lecturer(lecturer1, "Java", 8))
print(student2.rate_lecturer(lecturer2, "Python", 7))
print(student2.rate_lecturer(lecturer2, "Python", 8))
print(student2.rate_lecturer(lecturer2, "C#", 9))

print("\n--- Информация о студентах ---")
print(student1)
print(student2)

print("\n--- Информация о лекторах ---")
print(lecturer1)
print(lecturer2)

print("\n--- Информация о ревьюерах ---")
print(reviewer1)
print(reviewer2)


all_students = [student1, student2]
all_lecturers = [lecturer1, lecturer2]

print("\n--- Средние оценки за домашнее задание по курсам ---")
print(f"Средняя оценка за домашнее задание по Python: {average_hw_grade(all_students, 'Python')}")
print(f"Средняя оценка за домашнее задание по Java: {average_hw_grade(all_students, 'Java')}")
print(f"Средняя оценка за домашнее задание  по C#: {average_hw_grade(all_students, 'C#')}")

print("\n--- Средние оценки за лекции по курсам ---")
print(f"Средняя оценка за лекции по Python: {average_lecturer_grade(all_lecturers, 'Python')}")
print(f"Средняя оценка за лекции по Java: {average_lecturer_grade(all_lecturers, 'Java')}")
print(f"Средняя оценка за лекции по C#: {average_lecturer_grade(all_lecturers, 'C#')}")

