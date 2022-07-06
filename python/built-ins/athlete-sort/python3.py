#!/bin/python3

import math
import os
import random
import re
import sys

# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     k = int(input())
    
#     arr_temp = []
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j][k] > arr[j+1][k]:
#                 arr_temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = arr_temp
#     [print(" ".join(map(str, arr_elem))) for arr_elem in arr]


# best and simplest way
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

s = sorted(arr, key = lambda x: x[k])

[print(str.join(' ', map(str, s[i]))) for i in range(n)]
