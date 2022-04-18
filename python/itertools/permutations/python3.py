# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == "__main__":
    s, k = input().split()
    list_out = list(permutations(s, k))
    list_out.sort()
    for iter in list_out:
        print(''.join(iter))

# more simpler solution

# s, k = input().split()
# [print(''.join(p)) for p in sorted(list(permutations(s, int(k))))]