def p(g):
  a=[[0]*3 for _ in(0,0,0)]
  for r,row in enumerate(g):
    for c,v in enumerate(row):
      if v==5:
        for i in(-1,0,1):
          for j in(-1,0,1):
            try:
              x=g[r+i][c+j]
              if x:a[i+1][j+1]=x
            except:0
        return a