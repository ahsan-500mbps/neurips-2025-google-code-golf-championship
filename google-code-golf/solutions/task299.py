def p(g):
 R=range;h,w=len(g),len(g[0])
 for y in R(h):
  if 2 in (g[y][0],g[y][-1]):
   for x in R(w):
    v=g[y][x];g[y][x]=2 if v==0 else (v if v==2 else 4)
 for x in R(w):
  if 8 in (g[0][x],g[-1][x]):
   for y in R(h):
    v=g[y][x];g[y][x]=8 if v==0 else (v if v==8 else 4)
 return g