def p(g):
    n,m=len(g),len(g[0])
    a=[(i,j)for i in range(n)for j in range(m)if g[i][j]]
    if not a:return []
    r=min(i for i,j in a)
    R=max(i for i,j in a)
    c=min(j for i,j in a)
    C=max(j for i,j in a)
    h=[r]+[i+1 for i in range(r,R)if any(g[i][j]!=g[i+1][j]for j in range(c,C+1))]+[R+1]
    v=[c]+[j+1 for j in range(c,C)if any(g[i][j]!=g[i][j+1]for i in range(r,R+1))]+[C+1]
    return [[g[h[p]][v[q]]for q in range(len(v)-1)]for p in range(len(h)-1)]