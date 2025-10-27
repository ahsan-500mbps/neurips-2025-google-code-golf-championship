p=lambda g:[[2 if g[y][x]==5 and all(0<=y+Y<10 and 0<=x+X<10 and g[y+Y][x+X]==5 for Y,X in((1,0),(-1,0),(0,1),(0,-1)))else g[y][x]for x in range(10)]for y in range(10)]
