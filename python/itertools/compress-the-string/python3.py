from itertools import groupby

groups = [((len(list(g)), int(k))) for k, g in groupby(input())]
print(' '.join(map(str, groups)))


