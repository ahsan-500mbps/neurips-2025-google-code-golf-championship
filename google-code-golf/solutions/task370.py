def p(g):
    H,W=len(g),len(g[0])
    out=[r[:] for r in g]
    from collections import Counter
    bg=Counter(v for r in g for v in r).most_common(1)[0][0]
    color=[v for r in g for v in r if v not in (0,bg)][0]
    for i in range(H):
        for j in range(W):
            if g[i][j]==0:
                for k in range(i,H):
                    if out[k][j]==bg: out[k][j]=color
    return out
#Flagged