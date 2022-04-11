# easiest way

if __name__ == '__main__':
    len_M = int(input())
    set_M = set(map(int, input().split()))
    len_N = int(input())
    set_N = set(map(int, input().split()))
    
    set_sym_diff = set_M.symmetric_difference(set_N)
    arr_sym_diff = list(set_sym_diff)
    arr_sym_diff.sort()
    for arr_elem in arr_sym_diff:
        print(arr_elem)


# hardest way
# def symmetric_diff_print(set1, set2):
#     final_set = set()
#     diff_set1 = set1.difference(set2)
#     diff_set2 = set2.difference(set1)
#     final_set.update(diff_set1)
#     final_set.update(diff_set2)
#     arr_sorted = list(final_set)
#     arr_sorted.sort()
#     for arr_elem in arr_sorted:
#         print(arr_elem)


# if __name__ == '__main__':
#     len_M = int(input())
#     set_M = set(map(int, input().split()))
#     len_N = int(input())
#     set_N = set(map(int, input().split()))
#     symmetric_diff_print(set_M, set_N)
