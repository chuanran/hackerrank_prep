# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
S, k = input().split()
[print(''.join(elem)) for elem in combinations_with_replacement(sorted(S), int(k))]

# harder way using lamda

# from itertools import combinations_with_replacement
# s, k = input().split()
# combinations = sorted(map(lambda x: sorted(x), combinations_with_replacement(s, int(k))))
# [print(''.join(p)) for p in combinations]
    