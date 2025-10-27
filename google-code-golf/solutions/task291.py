def p(g):
 for y in range(len(g)-1):
  for x in range(len(g[0])-1):
   c=g[y][x:x+2]+g[y+1][x:x+2]
   for v in range(1,10):
    if c.count(v)==3 and 0 in c:return[[v]]