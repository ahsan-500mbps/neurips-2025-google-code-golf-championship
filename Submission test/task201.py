# TODO  # TO BE DONE BY Suhrid Sadman Abrar
def p(j,R=range,E=enumerate,N=next):
 F=[divmod(i,13)for i,v in E(sum(j,[]))if v==4];(k,W),(l,J),(a,_),_=F
 f=lambda r,c:r<1 or j[r-1][c]<1 or r>2 and j[r-1][c]==4 and j[r-2][c]>0
 C=N(u for r in zip(*j)if 4 not in r for u in r if u)
 e=N(i for i,r in E(j)if any(u==C and f(i,v)for v,u in E(r)))
 K=N(i for i,r in E(zip(*j))if any(u==C and f(v,i)for v,u in E(r)))
 for w in R(a-k-1):
  for L in R(J-W-1):
   j[k+w+1][[J-L-1,W+L+1][j[k+1][W]==C]],j[e+w][K+L]=j[e+w][K+L],0
 return[r[W:J+1]for r in j[k:a+1]]