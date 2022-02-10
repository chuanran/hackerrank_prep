# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
for i in range(int(N/2)):
    str = ".|."
    print(((i*2+1)*str).center(M, '-'))
print("WELCOME".center(M, '-'))
for i in range(int(N/2-1), -1, -1):
    str = ".|."
    print(((i*2+1)*str).center(M, '-'))
