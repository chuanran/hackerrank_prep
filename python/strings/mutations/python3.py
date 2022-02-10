def mutate_string(string, position, character):
    # first solution
    a = list(string)
    a[position] = character
    return ''.join(a)
    # second solution
    # return string[0:position] + character + string[position+1:]
