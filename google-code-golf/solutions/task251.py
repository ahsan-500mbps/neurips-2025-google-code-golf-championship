def p(a):
 h,w=len(a),len(a[0]);v=[[0]*w for _ in a]
 def f(i,j):
  if 0<=i<h>i-1 and 0<=j<w>j-1 and a[i][j]<1 and v[i][j]<1:v[i][j]=1;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(h):f(i,0);f(i,w-1)
 for j in range(w):f(0,j);f(h-1,j)
 return[[a[i][j]or(v[i][j]<1)for j in range(w)]for i in range(h)]