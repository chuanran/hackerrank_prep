cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    arr = []
    for i in range(n):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i-1] + arr[i-2])
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# newer version
# cube = lambda x: x ** 3

# def fibonacci(n):
    
#     f = [0, 1]

#     if n < 2:
#         return f[:n]

#     for i in range(n - 2):
#         f.append(f[i] + f[i + 1])

#     return f

# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))