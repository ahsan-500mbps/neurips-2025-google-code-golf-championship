# TODO  # TO BE DONE BY Suhrid Sadman Abrar
# task206.py
def p(g):
 t=list(zip(*g))
 nz=lambda a:[i for i,x in enumerate(a) if x]
 R=[set(nz(r)) for r in g]          # columns that have any color in each row
 C=[set(nz(c)) for c in t]          # rows that have any color in each col
 H,W=len(g),len(g[0])
 for v in range(1,10):              # per color, project within its own bands
  rr={i for i,r in enumerate(g) if v in r}
  cc={j for j,c in enumerate(t) if v in c}
  if not rr or not cc: continue
  for i in rr:
   # copy v across columns where this row intersects ANY occupied column of those columns that already contain v somewhere
   cols=sorted(Cj for j in cc for Cj in (R[i]&{j}) or ())
   for j in cols: g[i][j]=v
  for j in cc:
   # copy v down rows where this column intersects ANY occupied row of those rows that already contain v somewhere
   rows=sorted(Ri for i in rr for Ri in (C[j]&{i}) or ())
   for i in rows: g[i][j]=v
 return g
#FLAGGED