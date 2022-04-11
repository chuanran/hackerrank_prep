# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    num_eng_sub = int(input())
    set_eng_sub = set(map(int, input().split()))
    num_french_sub = int(input())
    set_french_sub = set(map(int, input().split()))
    set_diff_eng_fren_sub = set_eng_sub.difference(set_french_sub)
    print(len(set_diff_eng_fren_sub))