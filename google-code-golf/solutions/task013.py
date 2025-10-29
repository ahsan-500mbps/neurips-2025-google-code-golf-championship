def p(j,R=range):
 h,w=len(j),len(j[0])
 P=sorted((i,k,j[i][k])for i in R(h)for k in R(w)if j[i][k])
 if len(P)!=2:return j
 (r1,c1,a),(r2,c2,b)=P
 if r1==r2 or (r1==0 and r2==h-1):
  K=abs(c2-c1)
  for i in R(h):j[i][c1]=a;j[i][c2]=b
  if K:
   L=max(c1,c2)+K;t=[a,b] if c2>c1 else [b,a];x=0
   while L<w:
    for i in R(h):j[i][L]=t[x&1]
    L+=K;x+=1
 elif c1==c2 or (c1==0 and c2==w-1):
  K=abs(r2-r1)
  for k in R(w):j[r1][k]=a;j[r2][k]=b
  if K:
   i=max(r1,r2)+K;t=[a,b] if r2>r1 else [b,a];x=0
   while i<h:
    for k in R(w):j[i][k]=t[x&1]
    i+=K;x+=1
 return j
