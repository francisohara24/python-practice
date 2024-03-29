# Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Task:
# Dr.John Wesley has a spreadsheet containing a list of student's I Ds, marks, class and name.
# Your task is to help Dr. Wesley calculate the average marks of the students.
# Sum of all marks
# Average =
# Total Students
# Note:
# I. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
# Input Format
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, I Ds, name and class, under their respective column names.
# Constraints
# O < N < 100
# Output Format
# Print the average marks of the list corrected to 2 decimal places.

from collections import namedtuple

N = int(input())
columns = ",".join(input().split())

Student = namedtuple("Student", columns)
total_marks = 0

for i in range(N):
    details = input().split()
    student = Student(details[0], details[1], details[2], details[3])
    total_marks += float(student.MARKS)

average = total_marks / N
print(average)
