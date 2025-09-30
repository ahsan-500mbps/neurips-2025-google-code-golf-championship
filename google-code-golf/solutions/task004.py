def p(j,A=enumerate):
 c=[[0]*len(j[0])for _ in j]
 for e in {*sum(j,[])}-{0}:
  k=[(i,a)for i,r in A(j)for a,x in A(r)if x==e];w=max(i for i,_ in k);l=max(a for _,a in k)
  for i,a in k:c[i][a+(i<w and a<l)]=e
 return c
