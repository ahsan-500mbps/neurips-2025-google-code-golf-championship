def p(g):
 R=range;C=sum(g,[]).count(2)
 for _ in R(4):
  g=[*map(list,zip(*g[::-1]))];h=len(g)
  for r in R(h):
   if g[r].count(2)==C and sum(g[r])==2*C:
    for y in R(max(r,h-r)):
     if 0<=r+y<h and 2 not in g[r+y] and sum(g[r+y]):
      if 0<=r-y+1<h:g[r-y+1]=g[r+y][:]
     elif 0<=r-y-1<h and 0<=r+y<h:g[r+y]=g[r-y-1][:]
 g=[[3 if c==0 else c for c in r]for r in g];return g
