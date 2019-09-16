from student_report import Student_Reports
from cohort_report import Cohort_Report
from exercise_report import Exercise_Report
from instructor_report import Instructor_Report

Cohort_Report = Cohort_Report()
Cohort_Report.all_cohorts()

Student_Reports = Student_Reports()
Student_Reports.all_students()

Exercise_Report = Exercise_Report()
Exercise_Report.all_exercises()

Instructor_Report = Instructor_Report()
Instructor_Report.all_instructors()
