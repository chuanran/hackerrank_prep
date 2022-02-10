def swap_case(s):
    # can directly use swapcase to achieve it
    # return s.swapcase(). 
    str = ""
    for i in s:
        if i.isupper():
            str += i.lower()
        else:
            str += i.upper()
    return str