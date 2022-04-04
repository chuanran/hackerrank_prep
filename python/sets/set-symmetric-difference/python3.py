def symmetric_diff_print(set1, set2):
    final_set = set()
    diff_set1 = set1.difference(set2)
    diff_set2 = set2.difference(set1)
    final_set.update(diff_set1)
    final_set.update(diff_set2)
    print(final_set)
    arr_sorted = list(final_set)
    arr_sorted.sort()
    for arr_elem in arr_sorted:
        print(arr_elem)


if __name__ == '__main__':
    len_M = int(input())
    set_M = set(map(int, input().split()))
    len_N = int(input())
    set_N = set(map(int, input().split()))
    symmetric_diff_print(set_M, set_N)
