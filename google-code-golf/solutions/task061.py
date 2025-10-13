def p(j,u=enumerate):
 r=range;H=len(j);W=len(j[0]);f=lambda a,b:a*b<1 or a==b
 X=next((k for k in r(1,W)if all(f(a,b)for t in j for a,b in zip(t,t[k:]))),W)
 Y=next((k for k in r(1,H)if all(f(a,b)for s,t in zip(j,j[k:])for a,b in zip(s,t))),H)
 d={(i%Y,k%X):a for i,t in u(j) for k,a in u(t) if a}
 for i,t in u(j):
  for k,a in u(t):
   if not a:t[k]=d[i%Y,k%X]
 return j