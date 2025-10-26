def p(j):
 R=range;C=[x for x in R(len(j[0]))if any(r[x]==5 for r in j)]
 Rw=[y for y in R(len(j))if j[y][C[0]]==5]
 y0,y1=min(Rw)-1,max(Rw)+1;x0,x1=C[0],C[1]
 return[[r[x]for x in R(x0,x1+1)]for r in j[y0:y1+1]]

