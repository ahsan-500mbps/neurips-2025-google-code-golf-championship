def p(g):
 r=range(10)
 for i in r:
  for j in r:
   if g[i][j]==3:
    for d in[(1,1),(1,-1),(-1,1),(-1,-1)]:
     x,y=i+d[0],j+d[1]
     if 0<=x<10>y>=0 and g[x][y]==0:g[x][y]=8
 return g
#FLAGGED