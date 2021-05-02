class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'
    def aver(self):
        n = 0
        sum = 0
        for course, grades in self.grades.items():
            for gr in grades:
                n +=1
                sum += gr
        if n != 0:
            return (sum / n)
        else:
            print('Студент не получил еще ни одной оценки')
            return 0


    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за домашние задания: ' + str(
                self.aver()) + '\n' + 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\n' + 'Завершенные курсы: ' + ', '.join(self.finished_courses)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
        return self.aver() < other.aver()
    def aver_course(self, students_list, course):
        sum = 0
        n = 0
        for student in students_list:
            for courses, grades in student.grades.items():
                if courses == course:
                    for grade in student.grades[course]:
                        sum += grade
                        n += 1
        if n != 0:
            return (sum / n)
        else:
            print('Никто не получал оценки по этому курсу')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
    def aver(self):
        sum = 0
        n =0
        for grade in self.grades:
            sum += grade
            n += 1
        if n != 0:
            return (sum / n)
        else:
            print('Никто не оценил этого лектора')
            return 0


    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за лекции: ' + str(self.aver())

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
        return self.aver() < other.aver()
    def aver_lecture(self, lecturers_list, course):
        sum = 0
        n = 0
        for lecturer in lecturers_list:
            if course in lecturer.courses_attached:
                sum += lecturer.aver()
                n += 1
        if n != 0:
            return (sum / n)
        else:
            print('Никто не оценил этот курс')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.students_list += [best_student]
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Nick', 'Evan', 'your_gender')
best_student_2.students_list += [best_student_2]
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Git']
best_student_2.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Ed', 'Bud')
cool_reviewer.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Anna', 'Bale')
cool_reviewer_2.courses_attached += ['Git']

cool_lecturer = Lecturer('James', 'Croll')
cool_lecturer.lecturers_list += [cool_lecturer]
cool_lecturer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('John', 'Don')
cool_lecturer_2.lecturers_list += [cool_lecturer_2]
cool_lecturer_2.courses_attached += ['Git']

best_student.rate_l(cool_lecturer, 'Python', 10)
best_student.rate_l(cool_lecturer, 'Python',7)
best_student.rate_l(cool_lecturer, 'Python', 10)
best_student_2.rate_l(cool_lecturer_2, 'Git', 10)
best_student_2.rate_l(cool_lecturer_2, 'Git',8)
best_student_2.rate_l(cool_lecturer_2, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 9)
cool_reviewer_2.rate_hw(best_student_2, 'Git', 9)
cool_reviewer_2.rate_hw(best_student_2, 'Git', 9)



print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(cool_lecturer_2)
print(best_student_2)
print(best_student < best_student_2)
print(cool_lecturer < cool_lecturer_2)


print(cool_lecturer.aver_lecture(cool_lecturer.lecturers_list, 'Python'))
print(cool_lecturer.aver_lecture(cool_lecturer.lecturers_list, 'Git'))
print(best_student.aver_course(best_student.students_list, 'Python'))
print(best_student.aver_course(best_student.students_list, 'Git'))
