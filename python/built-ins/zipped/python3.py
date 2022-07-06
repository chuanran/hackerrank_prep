# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())
scores = [map(float, input().split()) for _ in range(x)]
scoreByStudents = list(zip(*scores))
[print((float)(sum(score_student)/x)) for score_student in scoreByStudents]