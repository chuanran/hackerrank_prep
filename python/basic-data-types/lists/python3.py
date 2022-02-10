if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cmd = input()
        if cmd.startswith("insert"):
            index = int(cmd.split()[1])
            num = int(cmd.split()[2])
            arr.insert(index, num)
        elif cmd.startswith("print"):
            print(arr)
        elif cmd.startswith("remove"):
            num = int(cmd.split()[1])
            arr.remove(num)
        elif cmd.startswith("append"):
            num = int(cmd.split()[1])
            arr.append(num)  
        elif cmd.startswith("sort"):
            arr.sort()
        elif cmd.startswith("pop"):
            arr.pop()      
        elif cmd.startswith("reverse"):
            arr.reverse()