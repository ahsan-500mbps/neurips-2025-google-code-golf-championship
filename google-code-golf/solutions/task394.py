# TODO  # TO BE DONE BY Nafis Fuad
L=len;R=range
def p(g):
 h,w=L(g),L(g[0]);Z=[(y,x)for y in R(h)for x in R(w)if g[y][x]==0]
 if not Z:return[[g[0][0]]]
 ys=[y for y,_ in Z];xs=[x for _,x in Z];y0,y1=min(ys),max(ys);x0,x1=min(xs),max(xs)
 def C(H,W):
  t=[[-1]*W for _ in R(H)]
  for y in R(h):
   for x in R(w):
    v=g[y][x]
    if v:
     r,c=y%H,x%W
     if t[r][c]<0:t[r][c]=v
     elif t[r][c]!=v:return
  for r in R(H):
   for c in R(W):
    if t[r][c]<0:t[r][c]=0
  return t
 T=None
 for H in R(1,h+1):
  for W in R(1,w+1):
   T=C(H,W)
   if T:break
  if T:break
 if not T:T=C(h,w)
 return[[T[y%L(T)][x%L(T[0])]for x in R(x0,x1+1)]for y in R(y0,y1+1)]