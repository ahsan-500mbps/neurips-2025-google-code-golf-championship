def p(j):
 R=range;n=len(j);e=[r[:]for r in j]
 for k in R(n):
  if j[1][k]==j[-2][k]==0 and sum(j[i][k]for i in R(1,n-1))<1:
   for i in R(1,n-1):e[i][k]=3
 for i in R(n):
  if j[i][1]==j[i][-2]==0 and sum(j[i][k]for k in R(1,n-1))<1:
   for k in R(1,n-1):
    if not e[i][k]:e[i][k]=3
 return e