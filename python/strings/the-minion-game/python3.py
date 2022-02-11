def minion_game(string):
    # your code goes here
    vowels_arr = ["A", "E", "I", "O", "U"]
    kevin_vowel_substr_count = 0
    stuart_consanant_substr_count = 0
    string_len = len(string)
    for index, alpha in enumerate(string):
        # alpha is a vowel
        if alpha.upper() in vowels_arr:
            kevin_vowel_substr_count += string_len - index
        else:
            stuart_consanant_substr_count += string_len - index
    if stuart_consanant_substr_count == kevin_vowel_substr_count:
        str = "Draw"
    elif stuart_consanant_substr_count > kevin_vowel_substr_count:
        str = f"Stuart {stuart_consanant_substr_count}"
    else:
        str = f"Kevin {kevin_vowel_substr_count}"
    print(str)

if __name__ == '__main__':
    s = input()
    minion_game(s)