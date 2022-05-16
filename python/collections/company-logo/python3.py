#!/bin/python3

from collections import OrderedDict

if __name__ == '__main__':
    s = input()
    # sort the string first to ensure for key's ASC
    sorted_arr = sorted(s)
    ordered_dict = OrderedDict()
    for i in sorted_arr:
        if i in ordered_dict:
            ordered_dict[i] += 1
        else:
            ordered_dict[i] = 1
    # pay attention to -l[1], that means reverse is true for value
    for k, v in sorted(ordered_dict.items(), key=lambda l: -l[1])[0:3]:
        print(k, v)

## a more concise way?

# from collections import OrderedDict

# company_name = input()
# letters = dict()

# for c in company_name:

#     if c in letters:
#         letters[c] += 1
#     else:
#         letters[c] = 1

# # sort by value DESC, then key ASC
# s = sorted(letters.items(), key=lambda l: (-l[1], l[0]))

# [print(s[i][0], s[i][1]) for i in range(3)]