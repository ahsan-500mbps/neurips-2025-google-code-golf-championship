def p(g):
 R=range;h,w=len(g),len(g[0]);x=0
 if 5 not in g[0]:g=[list(r)for r in zip(*g[::-1])];x=3
 c=g[0].count(5);s=g[0].index(5);X=[r[:]for r in g]
 g=[[5 if v==5 else 0 for v in r]for r in g]
 for y in R(h):
  L=sum(v>0 for v in X[y][:s]);Rr=sum(v>0 for v in X[y][s+c:])
  g[y]=g[y][:s-L]+[5]*(c+L+Rr)+g[y][s+c+Rr:]
 for _ in R(x):g=[list(r)for r in zip(*g[::-1])]
 return g