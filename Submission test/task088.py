from collections import Counter as C
def p(g):
 R=range;h,w=len(g),len(g[0])
 k=[v for v,n in C(x for r in g for x in r).items()if n==4][0]
 P=[(y,x)for y in R(h)for x in R(w)if g[y][x]==k]
 y0,y1=min(y for y,_ in P)+1,max(y for y,_ in P)
 x0,x1=min(x for _,x in P)+1,max(x for _,x in P)
 g=[r[x0:x1]for r in g[y0:y1]]
 for y in R(len(g)):
  for x in R(len(g[0])):
   if g[y][x]:g[y][x]=k
 return g