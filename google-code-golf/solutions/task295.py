def p(g):
 g=g[0];c=g[0];t=sum(x>0 for x in g)
 h=len(g)//2;w=len(g)
 r=[[0]*w for _ in range(h)]
 for y in range(h):
  for x in range(t):r[y][x]=c
  t+=1
 return r