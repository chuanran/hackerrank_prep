def cal_happiness(arr, seta, setb):
    happiness = 0
    for arr_elem in arr:
        if arr_elem in seta:
            happiness += 1
        if arr_elem in setb:
            happiness -= 1
    return happiness
    
    

if __name__ == "__main__":
    size_arr = list(map(int, input().split()))
    len_arr, len_set = size_arr[0], size_arr[1]
    arr = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    happiness = cal_happiness(arr, set_a, set_b)
    print(happiness)


