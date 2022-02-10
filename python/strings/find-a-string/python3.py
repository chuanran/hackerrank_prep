def count_substring(string, sub_string):
    # hardest way
    # len_sub = len(sub_string)
    # count = 0
    # for index in range(len(string) - len_sub + 1):
    #     if string[index:index+len_sub] == sub_string:
    #         count = count + 1
    
    # easier way: use find
    count = 0
    next_index = 0
    while next_index < len(string) - len(sub_string) + 1:
        next_index = string.find(sub_string, next_index)
        if next_index != -1:
            count+=1
            next_index += 1
        else:
            break
    
    return count