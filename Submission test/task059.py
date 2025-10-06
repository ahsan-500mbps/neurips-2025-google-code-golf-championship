def p(j):
 c=range(11);k=[[0 if (i+1)%4 and (j+1)%4 else 5 for i in c] for j in c];W={f'{x}{y}':0 for x in'012'for y in'012'}
 for y,r in enumerate(j):
  for x,v in enumerate(r):
   if 0<v!=5:E=v;W[f'{y//4}{x//4}']+=1
 e=max(W.values())
 for y,r in enumerate(k):
  for x,v in enumerate(r):
   if not v and W[f'{y//4}{x//4}']==e:r[x]=E
 return k
