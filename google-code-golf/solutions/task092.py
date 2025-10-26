def p(g):
 R=range;h,w=len(g),len(g[0]);r=[x[:]for x in g]
 for y in R(h):
  X=C=None
  for x in R(w):
   v=g[y][x]
   if v:
    if X is not None and v==C:
     for i in R(X+1,x):r[y][i]=v
    X,C=x,v
 for x in R(w):
  Y=C=None
  for y in R(h):
   v=g[y][x]
   if v:
    if Y is not None and v==C:
     for i in R(Y+1,y):r[i][x]=v
    Y,C=y,v
 return r