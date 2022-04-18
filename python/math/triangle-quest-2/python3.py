for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int((10 ** i) / 9) ** 2)


# the harder way from the answer
# for i in range(1,int(input())):
#     print(int(i*(10**(i-1))+i*(10**(i-2))+i*(10**(i-3))+i*(10**(i-4))+i*(10**(i-5))+i*(10**(i-6))+i*(10**(i-7))+i*(10**(i-8))+i*(10**(i-9))))