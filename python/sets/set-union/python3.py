# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    num_english_sub = int(input())
    set_eng_sub = set(map(int, input().split()))
    num_french_sub = int(input())
    set_fren_sub = set(map(int, input().split()))
    set_eng_french = set_eng_sub.union(set_fren_sub)
    print(len(set_eng_french))