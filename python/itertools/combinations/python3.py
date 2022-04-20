# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
str, a = input().split()
for i in range(1, int(a) + 1):
    [print(''.join(elem)) for elem in list(combinations(sorted(str), i))]


# harder way
# from itertools import combinations

# s, k = input().split()

# for i in range(int(k)):
#     [print(''.join(p)) for p in sorted(map(lambda x: sorted(x), combinations(s, i + 1)))]
