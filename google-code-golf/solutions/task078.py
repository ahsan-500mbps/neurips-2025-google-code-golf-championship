def p(j):
 R=range;a=len(j);b=len(j[0]);k=[[0]*b for _ in R(a)]
 for x in R(b):v=[j[y][x]for y in R(a)if j[y][x]];[k[i].__setitem__(x,v[i])for i in R(len(v))]
 return k