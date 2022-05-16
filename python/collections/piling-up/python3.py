# The initial idea from myself
# from collections import deque
# t = int(input())
# for _ in range(0, t):
#     de_que = deque()
#     n = int(input())
#     [de_que.append(i) for i in map(int, input().split())]
#     flag = True
#     tail_number = 0
#     for i in range(0, n):
#         if i == 0:
#             tail_number = de_que.popleft() if de_que[0] > de_que[-1] else de_que.pop()
#         else:
#             if de_que[0] > tail_number and de_que[-1] > tail_number:
#                 print("No")
#                 flag = False
#                 break
#             elif de_que[0] <= tail_number and de_que[-1] <= tail_number:
#                 tail_number = de_que.popleft() if de_que[0] > de_que[-1] else de_que.pop()
#             else:
#                 tail_number = de_que.popleft() if de_que[0] <= tail_number else de_que.pop()
#     if flag:
#         print("Yes")


# simpler solution:

# for i in range(int(input())):
    
#     n = int(input())
    
#     cubes = list(map(int, input().split()))
    
#     stack = 2 ** 31

#     for j in range(n):

#         if cubes[0] >= cubes[len(cubes) - 1] and cubes[0] <= stack:
#             stack = cubes.pop(0)
#         elif cubes[len(cubes) - 1] <= stack:
#             stack = cubes.pop()
#         else:
#             stack = 0
#             break

#     print('Yes' if stack > 0 else 'No')

# The best way for myself. we can use deque or list, both should work
from collections import deque
t = int(input())
for _ in range(0, t):
    de_que = deque()
    n = int(input())
    [de_que.append(i) for i in map(int, input().split())]
    flag = True
    tail_number = 2 ** 31
    for i in range(0, n):
        if de_que[0] > tail_number and de_que[-1] > tail_number:
                print("No")
                flag = False
                break
        elif de_que[0] <= tail_number and de_que[-1] <= tail_number:
            tail_number = de_que.popleft() if de_que[0] > de_que[-1] else de_que.pop()
        else:
            tail_number = de_que.popleft() if de_que[0] <= tail_number else de_que.pop()
    if flag:
        print("Yes")