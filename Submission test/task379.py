L=len
R=range
P=[[0,1],[0,-1],[1,0],[-1,0]]
def p(g):
 for i in range(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(h):
   if g[r].count(8)==w:
    g[r][0]=4
 return g
#FLAGGED