import sqlite3

class Student_Workload:

    def __init__(self):
        self.db_path = "/Users/DannyBarker/workspace/student_excercises_python/studentexercises.db"

    def student_practices(self):
        student_dict = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                e.Name
            from Student s
            join Working w on w.StudendId = s.Id
            join Exercise e on e.Id = w.ExerciseId
            """)

            student_practices = db_cursor.fetchall()

            for row in student_practices:
                student_name = f'{row[1]} {row[2]}'
                exercise_name = row[3]

                if student_name not in student_dict:
                    student_dict[student_name] = [exercise_name]
                else:
                    student_dict[student_name].append(exercise_name)

            for student, exercises in student_dict.items():
                print(f'{student} is woring on:')
                for exercise in exercises:
                    print(f'  * {exercise}')
