def p(j):
 a={};r=range(10)
 for y in r:
  for x in r:
   v=j[y][x]
   if v:a[v]=a.get(v,0)+1
 w=[k for k,v in a.items()if v==1][0]
 y,x=[(y,x)for y in r for x in r if j[y][x]==w][0]
 g=[[0]*10 for _ in r];g[y][x]=w
 for dy in(-1,0,1):
  for dx in(-1,0,1):
   if dy or dx:
    Y,X=y+dy,x+dx
    if 0<=Y<10 and 0<=X<10:g[Y][X]=2
 return g