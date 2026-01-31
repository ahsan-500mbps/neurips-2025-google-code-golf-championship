def p(c):
 R=range;h,w=len(c),len(c[0]);Y=[];X=[]
 for y in R(h-4):
  for x in R(w-4):
   if sum(c[y+i][x+j]==1 for i in R(5) for j in R(5))==16:Y+=[y+2];X+=[x+2]
 for y in R(h):
  for x in R(w):
   if y in Y or x in X:
    if c[y][x]!=1:c[y][x]=6
 return c