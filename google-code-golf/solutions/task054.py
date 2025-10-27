def p(g):
 o=[r[:]for r in g];B=g[0][0];V=set();C=[]
 for R in range(30):
  for S in range(30):
   if g[R][S]!=B and(R,S)not in V:
    q=[(R,S)];c=[]
    while q:
     r,s=q.pop(0);V.add((r,s));c+=[(r,s)]
     for d in(-1,0,1):
      for e in(-1,0,1):
       if d or e:
        x,y=r+d,s+e
        if 0<=x<30>~y and g[x][y]!=B and(x,y)not in V:q+=[(x,y)]
    if len(c)>1:C+=[c]
 f=min(C,key=len)
 R,S=zip(*f);r,s=(min(R)+max(R))//2,(min(S)+max(S))//2;m=g[r][s]
 P={(a-r,b-s):g[a][b]for a,b in f};T=set(f)
 for x,y in[(x,y)for x in range(30)for y in range(30)if g[x][y]==m and(x,y)not in T]:
  for(d,e),v in P.items():
   if(d==0 or e==0)and(d*2,e*2)in P:
    for k in range(1,30):
     a,b=x+d*k,y+e*k
     if not(0<=a<30>~b and o[a][b]!=B):break
     o[a][b]=v
   else:
    a,b=x+d,y+e
    if 0<=a<30>~b and o[a][b]!=B:o[a][b]=v
 for r,c in f:o[r][c]=B
 return o