
if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        action_str_arr = input().split()
        if "pop" in action_str_arr:
            s.pop()
        elif "remove" in action_str_arr:
            s.remove(int(action_str_arr[1]))
        elif "discard" in action_str_arr:
            s.discard(int(action_str_arr[1]))
        else:
            print("not supported action")
    print(sum(s))