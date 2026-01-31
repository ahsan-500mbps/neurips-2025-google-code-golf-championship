def p(g,E=enumerate):
 P=[(r,c,v)for r,R in E(g)for c,v in E(R)if v not in(0,8)]
 for r,c,_ in P:g[r][c]=0
 z=P[0];P=[(r-z[0],c-z[1],v)for r,c,v in P]
 for r,R in E(g):
  for c,v in E(R):
   if v==8:
    g[r][c]=z[2]
    for dr,dc,dv in P:g[r+dr][c+dc]=dv
 return g