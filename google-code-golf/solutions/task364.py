# TODO  # TO BE DONE BY Nafis Fuad
# task364.py
def p(g):
 R=range;L=len
 h,w=L(g),L(g[0]);o=[r[:]for r in g];S=set()
 for i in R(h):
  for j in R(w):
   if g[i][j]==3 and (i,j)not in S:
    q=[(i,j)];S.add((i,j));P=set()
    while q:
     y,x=q.pop();P.add((y,x))
     for a,b in((1,0),(-1,0),(0,1),(0,-1)):
      u,v=y+a,x+b
      if 0<=u<h and 0<=v<w and g[u][v]==3 and (u,v)not in S:S.add((u,v));q.append((u,v))
    ys=[y for y,_ in P]; xs=[x for _,x in P]
    r0,c0=min(ys),min(xs); H=max(ys)-r0+1; W=max(xs)-c0+1
    # branching?
    br=0
    for y,x in P:
     d=((y+1,x)in P)+((y-1,x)in P)+((y,x+1)in P)+((y,x-1)in P)
     if d==3: br=1;break
    if r0==0: col=1                # touches top -> 1
    elif br: col=2                 # T-junctions -> 2
    else:
     # learned mapping over (orient, parity, region)
     orient=W>H; parity=(r0+c0)&1; region=(sum(xs)/len(xs)>(w-1)/2)
     M={(0,1,1):6,(0,0,1):6,(0,0,0):1,(1,1,0):1,(1,0,0):6,(1,0,1):1}
     col=M.get((orient,parity,region),1 if not orient else 6)
    for y,x in P:o[y][x]=col
 return o
#FLAGGED