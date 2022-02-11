#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    # Notice that here we have to use " " (with a space) if we do not want to remove the spaces
    words = s.split(" ")
    str_arr = [elem.capitalize() for elem in words]
    str = " ".join(str_arr)
    return str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()