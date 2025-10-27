def p(g):
 R=range;h,w=len(g),len(g[0])
 for y in R(h//2+1):
  for x in R(w):
   a,b=g[y][x],g[-y-1][x]
   if a==4:g[y][x]=b
   if b==4:g[-y-1][x]=a
 for y in R(h):
  for x in R(w//2+1):
   a,b=g[y][x],g[y][-x-1]
   if a==4:g[y][x]=b
   if b==4:g[y][-x-1]=a
 return g