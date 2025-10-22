import json

def f(g):
 h=len(g);w=len(g[0]);o=[r[:]for r in g];v=[[0]*w for _ in range(h)];c=[];i=[]
 for y in range(h):
  for x in range(w):
   if g[y][x]==5 and v[y][x]<1:
    r1=c1=y,x;r2,c2=y,x
    while c2+1<w and g[y][c2+1]==5:c2+=1
    r=y
    while r+1<h and all(g[r+1][c]==5 for c in range(c1,c2+1)):r+=1
    r2=r
    for a in range(r1,r2+1):
     for b in range(c1,c2+1):v[a][b]=1
    c+=[(r1,c1,r2,c2)]
 for r1,c1,r2,c2 in c:
  v2=[[0]*w for _ in range(h)]
  for y in range(r1+1,r2):
   for x in range(c1+1,c2):
    if g[y][x]!=5 and g[y][x]!=0 and v2[y][x]<1:
     t=g[y][x];a,b=y,x;d,e=y,x
     while e+1<c2 and g[y][e+1]==t:e+=1
     f=1;z=a
     while z+1<r2 and f:
      for q in range(b,e+1):
       if g[z+1][q]!=t:f=0;break
      if f:z+=1
     d=z
     for p in range(a,d+1):
      for q in range(b,e+1):v2[p][q]=1
     i+=[(a,b,d,e,t,r1,c1,r2,c2)]
 for a,b,d,e,t,A,B,C,D in i:
  for y in range(a,d+1):
   for x in range(b,e+1):o[y][x]=5
 if len(i)>1:
  a,b,d,e,t,A,B,C,D=i[0];h1=d-a+1;w1=e-b+1
  m,n,p,q,u,E,F,G,H=i[1];h2=p-m+1;w2=q-n+1
  for y in range(A+1,C-h2+2):
   for x in range(B+1,D-w2+2):
    if all(o[y+dy][x+dx]==5 for dy in range(h2) for dx in range(w2)):
     for dy in range(h2):
      for dx in range(w2):o[y+dy][x+dx]=u
     break
   else:continue
   break
  for y in range(E+1,G-h1+2):
   for x in range(F+1,H-w1+2):
    if all(o[y+dy][x+dx]==5 for dy in range(h1) for dx in range(w1)):
     for dy in range(h1):
      for dx in range(w1):o[y+dy][x+dx]=t
     break
   else:continue
   break
 return o
def p(g):return f(g)
#FLAGGED