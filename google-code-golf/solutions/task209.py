def p(g):
 R=range;L=len
 H,W=L(g),L(g[0])
 V=set();C=[]
 for i in R(H):
  for j in R(W):
   v=g[i][j]
   if v and v!=4 and (i,j)not in V:
    q=[(i,j)];V.add((i,j))
    ys=[i];xs=[j]
    while q:
      y,x=q.pop()
      for a,b in((1,0),(-1,0),(0,1),(0,-1)):
        u,v=y+a,x+b
        if 0<=u<H and 0<=v<W and g[u][v]==g[i][j] and (u,v)not in V:
          V.add((u,v));q.append((u,v));ys.append(u);xs.append(v)
    C.append((sum(ys)/L(ys),sum(xs)/L(xs),g[i][j]))
 C.sort()
 G=lambda A:([A[0]],[0]) if not A else (lambda c,idx: (c,idx))(*(__import__('functools').reduce(
   lambda s,y:(s[0]+[y],s[1]+([s[1][-1]+1] if y-s[0][-1]>2 else [s[1][-1]])),
   A[1:],([A[0]],[0]))))
 ys=[y for y,_,_ in C]; xs=[x for _,x,_ in C]
 ry,iy=G(sorted(set(int(y) for y in ys)))
 rx,ix=G(sorted(set(int(x) for x in xs)))
 Y={v:i for v,i in zip(ry,iy)}
 X={v:i for v,i in zip(rx,ix)}
 h,w=L(ry)*2+2,L(rx)*2+2
 o=[[0]*w for _ in R(h)]
 o[0][0]=o[0][-1]=o[-1][0]=o[-1][-1]=4
 for y,x,c in C:
  r=Y[int(y)]*2+1; k=X[int(x)]*2+1
  o[r][k]=o[r+1][k]=o[r][k+1]=o[r+1][k+1]=c
 return o
#FLAGGED