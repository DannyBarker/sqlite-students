import sqlite3

class Working_Report:

    def __init__(self):
        self.db_path = "/Users/DannyBarker/workspace/student_excercises_python/studentexercises.db"


    def all_working(self):
        working_dict = dict()
        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.ExerciseLanguage,
                s.Id,
                s.FirstName,
                s.LastName
            from Exercise e
            join Working w on w.ExerciseId = e.Id
            join Student s on s.Id = w.StudendId

            """)
            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[3]
                student_name = f'{row[4]} {row[5]}'

                if exercise_name not in working_dict:
                    working_dict[exercise_name] = [student_name]
                else:
                    working_dict[exercise_name].append(student_name)

            for exercise, students in working_dict.items():
                print(f'{exercise}: ')
                for student in students:
                    print(f'  *{student}')

