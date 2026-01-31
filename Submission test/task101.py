def p(g):
 for r in range(1,len(g)-1):
  for c in range(1,len(g[0])-1):
   if g[r][c]<1 and sum(g[r+i][c+j]in(2,5)for i in(-1,0,1)for j in(-1,0,1))>3:g[r][c]=7
 return g
#flagged