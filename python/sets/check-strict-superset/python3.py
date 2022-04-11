# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    set_a = set(map(int, input().split()))
    num_set_b = int(input())
    is_superset = True
    for _ in range(num_set_b):
        set_b = set(map(int, input().split()))
        if len(set_b.intersection(set_a)) != len(set_b) or len(set_b) == len(set_a):
            is_superset = False
    print(is_superset)
            