def p(g):
    h, w = len(g), len(g[0])
    r = [row[:] for row in g]
    # Find bounding boxes of 4-blocks
    blocks = []
    vis = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j] == 4 and not vis[i][j]:
                q = [(i,j)]
                vis[i][j] = 1
                minr=maxr=i
                minc=maxc=j
                while q:
                    x,y = q.pop()
                    for X,Y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if 0<=X<h and 0<=Y<w and g[X][Y]==4 and not vis[X][Y]:
                            vis[X][Y]=1
                            q.append((X,Y))
                            minr=min(minr,X); maxr=max(maxr,X)
                            minc=min(minc,Y); maxc=max(maxc,Y)
                blocks.append((minr,maxr,minc,maxc))
    # Sort by vertical position (top first)
    blocks.sort()
    # Fill interiors
    for k,(r1,r2,c1,c2) in enumerate(blocks):
        fill = 1 if k == 0 else 2
        for i in range(r1+1, r2):
            for j in range(c1+1, c2):
                if g[i][j]==4:
                    r[i][j] = fill
    return r