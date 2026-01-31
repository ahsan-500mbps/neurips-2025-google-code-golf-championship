def p(g):
 t=[c for c in zip(*g) if 5 not in c];o=[]
 for c in t:
  v=[x for x in c if x]
  while v:o+=([v.pop(0)if v else 0,v.pop(0)if v else 0,0],)
 return [list(r) for r in zip(*o)] if o else [[0]*0,[0]*0,[0]*0]
#FLAGGED