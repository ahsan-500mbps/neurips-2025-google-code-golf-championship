def p(g):
 t=list(zip(*g))
 F=lambda a:{x for x in a if x}
 G=lambda a:(lambda s:(next(iter(s),0),len(s)==1))(F(a))
 rb=[v if ok else 0 for v,ok in map(G,g)]
 cb=[v if ok else 0 for v,ok in map(G,t)]
 rows=sum(v>0 for v in rb)>=sum(v>0 for v in cb)
 R={};C={}
 for i,v in enumerate(rb):
  if v:R.setdefault(v,[]).append(i)
 for j,v in enumerate(cb):
  if v:C.setdefault(v,[]).append(j)
 for i,r in enumerate(g):
  for j,x in enumerate(r):
   if x==0:
    if rows and rb[i]:
     for ii in R[rb[i]]: g[ii][j]=0
    elif not rows and cb[j]:
     for jj in C[cb[j]]: g[i][jj]=0
 return g