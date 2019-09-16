import sqlite3

class Instructor:

    def __init__(self, first_name, last_name, specialty, handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is an instructor for {self.cohort}.'


class Instructor_Report:

    def __init__(self):
        self.db_path =self.db_path = "/Users/DannyBarker/workspace/student_excercises_python/studentexercises.db"

    def all_instructors(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[4], row[6])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.specialty,
                i.SlackHandle,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            print("\nInstructor: \n")
            [print(f'  * {i}') for i in all_instructors]