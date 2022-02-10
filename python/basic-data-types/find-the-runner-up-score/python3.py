if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_orig = list(arr)
    max_val = max(arr_orig)
    arr_new = [i for i in arr_orig if i != max_val]
    print(max(arr_new))