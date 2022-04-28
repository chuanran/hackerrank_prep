# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://realpython.com/python-namedtuple/
from collections import namedtuple
n = int(input())
Student = namedtuple("Student", input())
sum = 0
for _ in range(0, n):
    row = input().split()
    student = Student(row[0], row[1], row[2], row[3])
    sum += int(student.MARKS)
print('%.2f' % (sum/n))