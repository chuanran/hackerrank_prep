def average(array):
    # your code goes here
    arr_set = set(array)
    len_arr_set = len(arr_set)
    sum_arr_set = sum(arr_set)
    return sum_arr_set/len_arr_set
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)