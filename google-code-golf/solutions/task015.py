L=len;R=range
def p(g):
 h,w=L(g),L(g[0])
 for r in R(h):
  for c in R(w):
   if g[r][c]==2:
    for a,b in(1,1),(-1,-1),(-1,1),(1,-1):
     try:g[r+a][c+b]=4
     except:0
   elif g[r][c]==1:
    for a,b in(0,1),(0,-1),(-1,0),(1,0):
     try:g[r+a][c+b]=7
     except:0
 return g
