import re

for _ in range(int(input())):

    text = input()

    for s, r in [('\&\&', 'and'), ('\|\|', 'or')]:
        # (?<= ) is a positive lookbehind that makes sure && is preceded by a space
        # (?= ) is a positive lookahead that makes sure && is followed by a space
        text = re.sub(r"(?<= )" + s + "(?= )", r, text)
    print(text)
