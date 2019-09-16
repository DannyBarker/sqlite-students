import sqlite3

class Exercise:

    def __init__(self, name, lang):
        self.exercise_name = name
        self.language = lang

    def __repr__(self):
        return f'"{self.exercise_name}"" is a {self.language} exercise.'

class Exercise_Report:

    def __init__(self):
        self.db_path = "/Users/DannyBarker/workspace/student_excercises_python/studentexercises.db"

    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.ExerciseLanguage
            from Exercise e
            """)
            all_exercises = db_cursor.fetchall()

            print("\nExercises: \n")
            print(f'  -- Javascript --')
            [print(f'   * {e}') for e in all_exercises if e.language == "Javascript"]
            print(f'  -- React --')
            [print(f'   * {e}') for e in all_exercises if e.language == "React"]