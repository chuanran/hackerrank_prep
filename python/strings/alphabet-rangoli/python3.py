def print_rangoli(size):
    # your code goes here
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    column_num = 4 * size - 3
    line_num = 2 * size - 1
    rangoli_arr = []
    for i in range(int(line_num/2 + 1)):
        center_str_arr = []
        reverse_str_arr = []
        len_center_str_arr = i * 2 + 1
        for j in range(int(len_center_str_arr/2 + 1)):
            center_str_arr.append(alpha_list[size - 1 -j])
        reverse_str_arr = center_str_arr[:-1]
        reverse_str_arr.reverse()
        center_str_arr.extend(reverse_str_arr)
        center_str = '-'.join(center_str_arr)
        all_str = center_str.center(column_num, '-')
        rangoli_arr.append(all_str)
        print(all_str)
    
    rangoli_arr_second_half = rangoli_arr[:-1]
    rangoli_arr_second_half.reverse()
    for arr_elem in rangoli_arr_second_half:
        print(arr_elem)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)