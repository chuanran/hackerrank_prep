if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tu = tuple(integer_list)
    print(hash(tu))