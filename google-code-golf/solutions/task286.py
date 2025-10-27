def p(g):
 R=range;h,w=len(g),len(g[0]);f=sum(g,[]);a,b=sorted(set(f),key=f.count)[:2];m={a:b,b:a}
 for _ in R(50):
  for y in R(h):
   for x in R(w):
    if g[y][x]in m:
     for Y,X in((1,0),(-1,0),(0,1),(0,-1)):
      ny,nx=y+Y,x+X
      if 0<=ny<h and 0<=nx<w and not g[ny][nx]:g[ny][nx]=m[g[y][x]]
 return g