if __name__ == '__main__':
    arr = []
    min_score = None
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if min_score is None or score <= min_score:
            min_score = score
        arr.append([name, score])
    arr_new = [elem for elem in arr if elem[1] != min_score]
    second_min_score = None
    for stu in arr_new:
        if second_min_score is None or stu[1] <= second_min_score:
            second_min_score = stu[1]
    arr_final = [elem[0] for elem in arr_new if elem[1] == second_min_score]
    for i in sorted(arr_final):
        print(i)