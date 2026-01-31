def p(j):
 c=[r[:]for r in j];E=[(y,x)for y in range(len(j))for x in range(len(j[0]))if j[y][x]==8]
 if E:
  Y=[y for y,_ in E];X=[x for _,x in E]
  for y in range(min(Y),max(Y)+1):
   for x in range(min(X),max(X)+1):
    if j[y][x]==1:c[y][x]=3
 return c

