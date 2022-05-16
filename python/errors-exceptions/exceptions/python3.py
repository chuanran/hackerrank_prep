t = int(input())
for _ in range(t):
    # make sure to include map (int) in the try block as well
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)