def order_function(letter):
    if letter.islower():
        return (0, letter)
    if letter.isupper():
        return (1, letter)
    return (2 if int(letter) % 2 != 0 else 3, letter)

print(*sorted(input(), key=order_function), sep='')


# a simpler solution
# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')


