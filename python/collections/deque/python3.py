# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for _ in range(0, n):
    cmd = input().split()
    if cmd[0] == "append":
        d.append(cmd[1])
    elif cmd[0] == "appendleft":
        d.appendleft(cmd[1])
    elif cmd[0] == "pop":
        d.pop()
    elif cmd[0] == "popleft":
        d.popleft()
print(' '.join(d))