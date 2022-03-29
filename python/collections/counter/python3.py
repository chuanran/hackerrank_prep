from collections import Counter
if __name__ == '__main__':
    num_shoes = int(input())
    shoes_size_list = [i for i in input().split()]
    num_customers = int(input())
    earned_total_money = 0
    counter_shoe_size_dict = dict(Counter(shoes_size_list))

    for _ in range(num_customers):
        size_price_arr = input().split()
        size, price = size_price_arr[0], int(size_price_arr[1])
        if size in counter_shoe_size_dict.keys() and counter_shoe_size_dict[size]>0:
            earned_total_money = earned_total_money + price
            d1 = {size: counter_shoe_size_dict[size]-1}
            counter_shoe_size_dict.update(d1)
    print(earned_total_money)
 


