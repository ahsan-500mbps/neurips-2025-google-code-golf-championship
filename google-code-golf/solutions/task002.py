def p(a):
 r=range;n=len(a);v=[[0]*n for _ in r(n)]
 def f(i,j):
  if 0<=i<n and 0<=j<n and a[i][j]<1 and v[i][j]<1:
   v[i][j]=1;[f(i+1,j),f(i-1,j),f(i,j+1),f(i,j-1)]
 [f(i,0)or f(i,n-1)or f(0,i)or f(n-1,i)for i in r(n)]
 return[[4 if a[i][j]<1 and v[i][j]<1 else a[i][j]for j in r(n)]for i in r(n)]