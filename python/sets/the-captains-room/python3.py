# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ =="__main__":
    K = int(input())
    arr_room_number = list(map(int, input().split()))
    set_room_number = set(arr_room_number)
    for room_num in set_room_number:
        if arr_room_number.count(room_num) == K:
            continue
        else:
            print(room_num)