def p(j,R=range,L=len):
 h,w=L(j),L(j[0]);x=j[0][2]
 E={(i,k)for i in R(h)for k in R(w)if j[i][k]==x}
 C=[r[:]for r in j]
 for i,k in E:C[i][k]=0
 for e in R(h):
  P=[(i,k)for i in R(h)for k in R(w)if C[i][k]==e]
  for i1,k1 in P:
   for i2,k2 in P:
    if i1==i2:a,b=sorted((k1,k2));C[i1][a:b+1]=[e]*(b-a+1)
    elif k1==k2:a,b=sorted((i1,i2));[C[t].__setitem__(k1,e)for t in R(a,b+1)]
 for i,k in E:C[i][k]=x
 return C
# FLAGGED