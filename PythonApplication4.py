class Student:
    def __init__(self, name, surname ):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []
    


    def __str__(self):
        def bege(a, x):
            if len(a) == 1:
               return ' '.join([str(i) for i in x])
            else:
               return ', '.join([str(i) for i in x])
                
        res = f"Студент:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задание: {sum(self.grades)/len(self.grades)}\nКурсы в процессе изучения: {bege(self.grades, self.courses_in_progress)}\nЗавершенные курсы: {bege(self.grades, self.finished_courses)}"
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.Grades_for_lectures = []
        self.grade = []

        

class Lecturer (Mentor):
    def grads(self):
        super().grades_for_lectures = []
        
    def __str__ (self):
        res = f"Лектор:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(self.grades_for_lectures)/len(self.grades_for_lectures)} "
        return res

class Reviewer (Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
       

        
    def __str__ (self):
        res = f"Проверяющий:\nИмя: {self.name}\nФамилия: {self.surname}"
        return res
        
        
        

cool_lectures = Lecturer ('Billy', 'Djin',)
cool_lectures.grades_for_lectures = [10, 10 , 10 ,9]
cool_reviewer = Reviewer ('Billy', 'Herrington')
cool_reviewer.grade = [10, 9, 10, 9] 

some_student = Student ('Ruoy', 'Eman')
some_student.finished_courses = ['Введение в программирование']
some_student.courses_in_progress = ['Python', 'Git']
some_student.grades = [10, 10, 9, 8, 10]
print (cool_reviewer)
print ()
print ()
print (cool_lectures)
print ()
print ()
print (some_student)







