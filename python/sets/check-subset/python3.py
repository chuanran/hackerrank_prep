# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        len_set_a = int(input())
        set_a = set(map(int, input().split()))
        len_set_b = int(input())
        set_b = set(map(int, input().split()))
        print(set_a.intersection(set_b) == set_a)
