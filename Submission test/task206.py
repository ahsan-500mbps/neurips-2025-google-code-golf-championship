def p(g):
 t=list(zip(*g))
 nz=lambda a:[i for i,x in enumerate(a) if x]
 R=[set(nz(r)) for r in g]
 C=[set(nz(c)) for c in t]
 H,W=len(g),len(g[0])
 for v in range(1,10):
  rr={i for i,r in enumerate(g) if v in r}
  cc={j for j,c in enumerate(t) if v in c}
  if not rr or not cc: continue
  for i in rr:
   cols=sorted(Cj for j in cc for Cj in (R[i]&{j}) or ())
   for j in cols: g[i][j]=v
  for j in cc:
   rows=sorted(Ri for i in rr for Ri in (C[j]&{i}) or ())
   for i in rows: g[i][j]=v
 return g
#FLAGGED