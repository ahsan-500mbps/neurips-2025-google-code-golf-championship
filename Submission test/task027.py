L=len
R=range
def p(g):
 h,w=L(g),L(g[0])
 for r in R(1,h-1):
  for c in R(w//2-1):
   try:
    if g[r+1][c]==0 and g[-(r+2)][-(c+1)]>0:g[r+1][c]=2
   except:0
 return g
#FLAGGED