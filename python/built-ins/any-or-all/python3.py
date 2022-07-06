# harder way to check palindromic number
# def palindromic(number):
#     number = str(number)
#     num_len = (int)(len(str(number)))
#     return number[0:(int)(num_len/2)] == number[num_len-1:(int)(num_len/2):-1]

def palindromic(number):
    number_lst = list(str(number))
    return ''.join(reversed(number_lst)) == ''.join(number_lst)

n = input()
arr = list(map(int, input().split()))
print(all([elem >= 0 for elem in arr]) and any([palindromic(number) for number in arr]))


# solution from github
# def palindromic(n):
#     nlist = list(str(n))
#     return str.join('', nlist) == str.join('', reversed(nlist))

# input()
# numbers = list(map(int, input().split()))

# is_palindromic = [palindromic(x) for x in numbers]
# is_positive = [x >= 0 for x in numbers]

# print(all(is_positive) and any(is_palindromic))
