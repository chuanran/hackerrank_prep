# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    len_set_a = int(input())
    set_a = set(map(int, input().split()))
    num_sets_pairs = int(input())
    for _ in range(num_sets_pairs):
        action_arr = input().split()
        new_set = set(map(int, input().split()))
        if "intersection_update" == action_arr[0]:
            set_a.intersection_update(new_set)
        elif "update" == action_arr[0]:
            set_a.update(new_set)
        elif "symmetric_difference_update" == action_arr[0]:
            set_a.symmetric_difference_update(new_set)
        elif "difference_update" == action_arr[0]:
            set_a.difference_update(new_set)
    print(sum(set_a))