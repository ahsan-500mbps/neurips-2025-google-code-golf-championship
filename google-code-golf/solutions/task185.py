def p(g):
    from collections import Counter
    b = Counter(x for r in g for x in r).most_common(1)[0][0]
    a = [x for r in g for x in r if x != b]
    r = [[0]*3 for _ in range(3)]
    for i, v in enumerate(dict.fromkeys(a)): r[i//3][i%3] = v
    return r

#Flagged