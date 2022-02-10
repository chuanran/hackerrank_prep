if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_score = student_marks[query_name]
    sum = 0.00
    for score in list_score:
        sum = sum + score
    print(format(sum/len(list_score), ".2f"))