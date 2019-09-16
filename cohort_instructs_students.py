import sqlite3

class Cohort_Instructs_Students:

    def __init__(self):
        self.db_path = "/Users/DannyBarker/workspace/student_excercises_python/studentexercises.db"

    def cohort_people(self):
        cohort_dict = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name,
                s.FirstName StudentFirstName,
                s.LastName StudentLastName,
                i.FirstName,
                i.LastName
            from Cohort c
            join Student s on s.CohortId = c.Id
            join Instructor i on i.CohortId = c.Id
            """)

            cohort_people = db_cursor.fetchall()

            for row in cohort_people:
                student_name = f'{row[2]} {row[3]}'
                cohort_name = row[1]
                instructor_name = f'{row[4]} {row[5]}'

                if cohort_name not in cohort_dict:
                    cohort_dict[cohort_name]= {'Students': set(), 'Instructors': set()}
                    cohort_dict[cohort_name]['Students'].add(student_name)
                    cohort_dict[cohort_name]['Instructors'].add(instructor_name)
                else:
                    cohort_dict[cohort_name]['Students'].add(student_name)
                    cohort_dict[cohort_name]['Instructors'].add(instructor_name)

            for cohort, persons in cohort_dict.items():
                print(f'{cohort}: ')
                for type, peoples in persons.items():
                    print(f'  {type}: ')
                    for person in peoples:
                        [print(f'    *{person} is a student in {cohort}.') if type == "Students" else print(f'    *{person} is an instructor for {cohort}.')]