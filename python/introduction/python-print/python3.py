if __name__ == '__main__':
    n = int(input())
    string = "1"
    for i in range(2, n+1):
        string = string + str(i)
    print(string)