def p(j):
 n=len(j)
 for x in range(1,len(j[0])):j[n-1][x]=4;j[n-x-1][x]=2
 return j