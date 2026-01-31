#TODO  # TO BE DONE BY Nafis Fuad
def p(g):
 h,w=len(g),len(g[0])
 R=C=rs=cs=0
 for y in range(h):
  d={}
  for x in range(w):
   v=g[y][x]
   if v:d[v]=d.get(v,0)+1
  if d:
   m=max(d.values())
   if m>rs:rs=m;R=y
 for x in range(w):
  d={}
  for y in range(h):
   v=g[y][x]
   if v:d[v]=d.get(v,0)+1
  if d:
   m=max(d.values())
   if m>cs:cs=m;C=x
 o=[r[:] for r in g]
 for y in range(R-1,R+2):
  if 0<=y<h:
   for x in range(C-1,C+2):
    if 0<=x<w and(y!=R or x!=C):o[y][x]=4
 return o
