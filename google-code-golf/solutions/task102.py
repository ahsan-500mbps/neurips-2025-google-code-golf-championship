def p(g):
    for r in range(1,len(g)-1):
        for c in range(1,len(g[0])-1):
            if g[r][c]==0 and sum(g[r+dr][c+dc] in (2,5)
               for dr in(-1,0,1) for dc in(-1,0,1))>3:
                g[r][c]=2
    return g
#flagged