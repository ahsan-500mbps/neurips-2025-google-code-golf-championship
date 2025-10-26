def p(j):
 a=[r[:]for r in j]
 for x in range(5):
  for y in range(5):
   if j[y][x]==1:a[y][x]=0;a[4][x]=1
 return a