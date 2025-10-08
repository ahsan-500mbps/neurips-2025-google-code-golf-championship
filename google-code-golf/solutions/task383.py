# TODO  # TO BE DONE BY Nafis Fuad
R=range
L=len
def p(g):
 for i in R(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(1,h-1):
   for c in R(w):
    C=g[r][c];Z=g[r+1][c]
    if g[r-1][c]==Z and Z!=C and 0<Z<10 and 0<C<10:
     g[r][c]=Z
     for x in R(w):
      if g[r][x]==0:g[r][x]=C+10
      if g[r][x]==C:g[r][x]=Z+10
 g=[[c if c<10 else c-10 for c in r] for r in g]
 return g