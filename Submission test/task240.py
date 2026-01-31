def p(g):
    R=range;L=len
    h,w=L(g),L(g[0]);o=[r[:]for r in g]
    def Lz(i,j):
        for x in R(j-1,-1,-1):
            if g[i][x]:return g[i][x]
    def Rz(i,j):
        for x in R(j+1,w):
            if g[i][x]:return g[i][x]
    def Uz(i,j):
        for y in R(i-1,-1,-1):
            if g[y][j]:return g[y][j]
    def Dz(i,j):
        for y in R(i+1,h):
            if g[y][j]:return g[y][j]
    for i in R(1,h,2):
        for j in R(1,w,2):
            if o[i][j]:continue
            a=Lz(i,j); b=Rz(i,j); c=Uz(i,j); d=Dz(i,j)
            v = (c or d) if (i==1 or i==h-2) else (a or b)
            if not v:
                s=[x for x in (a,b,c,d) if x]
                if s:
                    from collections import Counter
                    v=Counter(s).most_common(1)[0][0]
            if v:o[i][j]=v
    return o
# FLAGGED