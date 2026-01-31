def f(a,p,y,c,x,v):
 for i in range(y,x+1):
  for j in range(p,c+1):a[i][j]=v
def z(a,p,y,c,x):
 f(a,p,y,c,x,4);f(a,p+1,y+1,c-1,x-1,2)
 a[y][p]=a[y][c]=a[x][p]=a[x][c]=1
def p(a):
 h,w=len(a),len(a[0])
 for i in range(h*w):
  x,y=i%w,i//w
  if a[y][x]==5:
   X,Y=x,y
   while X<w-1and a[Y][X+1]==5:X+=1
   while Y<h-1and a[Y+1][X]==5:Y+=1
   z(a,x,y,X,Y)
 return a
