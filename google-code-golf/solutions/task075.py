def p(j):
 R=range;a=[r[:]for r in j];e=[[j[y][x]for x in R(3)]for y in R(3)]
 for y in R(9):
  for x in R(4,13):
   if j[y][x]==1:
    for Y in R(-1,2):
     for X in R(-1,2):
      if 0<=y+Y<9and 4<=x+X<13:a[y+Y][x+X]=e[Y+1][X+1]
 return a