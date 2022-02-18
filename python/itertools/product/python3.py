from itertools import product
a = map(int, input().split())
b = map(int, input().split())
print(' '.join(list(map(str, product(a, b)))))