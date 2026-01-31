def p(a):
 h,w=len(a),len(a[0]);b=[r[:]for r in a]
 for i in range(h):
  for j in range(w):
   c=a[i][j]
   if c and(i<1 or j<1 or a[i-1][j-1]-c):
    k=0
    while i+k<h and j+k<w and a[i+k][j+k]==c:
     if k&1:b[i+k][j+k]=4
     k+=1
 return b
