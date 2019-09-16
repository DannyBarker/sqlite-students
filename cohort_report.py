import sqlite3

class Cohort:

    def __init__(self, name):
        self.Cohort_Name = name

    def __repr__(self):
        return f'{self.Cohort_Name}'

class Cohort_Report:

    def __init__(self):
        self.db_path = "/Users/DannyBarker/workspace/student_excercises_python/studentexercises.db"

    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Cohort(row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()
            print("\nCohorts: \n")
            [print(f'  * {c}') for c in all_cohorts]