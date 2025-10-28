def p(p,n=range):
 i=len(p);R=lambda q:[*map(list,zip(*q[::-1]))]
 for k in n(4):
  x,y=zip(*[(a,b)for a in n(i) for b in n(i) if p[a][b]])
  a,b,c,d=min(x),max(x),min(y),max(y);t=p[a][c];q=p[a].count(t)
  if q<p[b].count(t):
   L,Rr=c+q//2,d-q//2
   for u in n(b):p[u][L:Rr+1]=[4]*(Rr-L+1)
   for u in n(a+1,b):p[u][c+1:d]=[4]*(d-c-1)
   for u in n(a+1):
    v=a-u;(L>=u)and p[v].__setitem__(L-u,4);(Rr+u<i)and p[v].__setitem__(Rr+u,4)
   for _ in n(4-k):p=R(p)
   return p
  p=R(p)