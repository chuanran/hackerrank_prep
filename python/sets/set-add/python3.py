# Enter your code here. Read input from STDIN. Print output to STDOUT
  
if __name__ == "__main__":
    num_stamps = int(input())
    country_stamp_set = set()
    for _ in range(num_stamps):
        country_stamp_set.add(input())
    print(len(country_stamp_set))
    