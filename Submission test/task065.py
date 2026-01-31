def p(j):
 A=range;c=(len(j)-1)//2
 if c==1:
  E=[j[0][0],j[0][2],j[2][0],j[2][2]]
  for k in E:
   if E.count(k)==1:return[[k]]
 for y,x in((0,0),(0,c+1),(c+1,0),(c+1,c+1)):
  J=[[j[y+r][x+c]for c in A(c)]for r in A(c)]
  k=[v for r in J for v in r]
  if len(set(k))>1:return J
