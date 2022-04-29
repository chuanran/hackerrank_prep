# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
ordered_dict = OrderedDict()
for _ in range(0, n):
    item_str = input().split()
    price = int(item_str[-1])
    item_name = " ".join(item_str[:-1])
    if item_name in ordered_dict:
        ordered_dict[item_name] += price
    else:
        ordered_dict[item_name] = price
for key,value in ordered_dict.items():
    print(key + " " + str(value))

# a new solution (similar way)

# from collections import OrderedDict

# ordinary_dictionary = OrderedDict()

# for _ in range(int(input())):

#     data = input().split()
#     price = int(data.pop())
#     name = ' '.join(data)

#     if name in ordinary_dictionary:
#         ordinary_dictionary[name] += price
#     else:
#         ordinary_dictionary[name] = price

# [print(item[0] + ' ' + str(item[1])) for item in ordinary_dictionary.items()]
    