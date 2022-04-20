# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
S = input().split()
K = int(input())
a_count = 0
total_count = 0
for tu in combinations(S, K):
    total_count += 1
    if 'a' in tu:
        a_count += 1
print(a_count/total_count)

# simpler way

# from itertools import combinations

# n = int(input())
# s = input().split()
# k = int(input())
# combinations = list(combinations(s, k))
# has_a = sum(1 for c in combinations if 'a' in c)
# print(has_a / len(combinations))