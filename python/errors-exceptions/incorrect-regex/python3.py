import re
t = int(input())
for _ in range(t):
    try:
        a = re.search(input(), '')
        print('True')
    except:
        print('False')