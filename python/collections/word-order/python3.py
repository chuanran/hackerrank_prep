# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
ordered_dict = OrderedDict()
for _ in range(0, n):
    data = input()
    if data not in ordered_dict:
        ordered_dict[data] = 1
    else:
        ordered_dict[data] += 1
print(len(ordered_dict))
print(' '.join(map(str, ordered_dict.values())))