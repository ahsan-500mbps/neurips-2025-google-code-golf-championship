L=len;R=range;E=enumerate
M=lambda m,C:sorted([[i,j]for i,r in E(m)for j,x in E(r)if x==C])
def p(g):
 S=sum(g,[])
 P=sorted((S.count(C),C)for C in R(9))
 d={k:M(g,k)for _,k in P[:-2]}
 Z=M(g,P[-2][1]);z=Z[0];h,w=L(g),L(g[0]);X=[r[:]for r in g]
 for C,v in d.items():
  if v:
   y,x=v[0][0]-z[0],v[0][1]-z[1];y-=y<0
   for m in R(1,10):
    a,b=y*m,x*m
    for i,j in Z:
     u,v=i+a,j+b
     if 0<=u<h and 0<=v<w:X[u][v]=C
 return X
# FLAGGED 