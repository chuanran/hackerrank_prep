# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
k, m = map(int, input().split())
n = [list(map(int, input().split()))[1:] for _ in range(k)]

arr = [sum(map(lambda x: x ** 2, i)) % m for i in list(product(*n))]
print(max(arr))

   
