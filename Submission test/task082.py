def p(j):
 a=[r[:]for r in j];h,w=len(j),len(j[0])
 for x in range(w):
  if j[0][x]:
   for y in range(h):
    v=j[0][x]
    if y%2==0:a[y][x]=v
    else:
     if x:a[y][x-1]=v
     if x<w-1:a[y][x+1]=v
 return a