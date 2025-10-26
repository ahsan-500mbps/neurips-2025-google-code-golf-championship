def p(g):
    h, w = len(g), len(g[0])
    r = [row[:] for row in g]
    visited = set()

    def bfs(i, j):
        q = [(i, j)]
        visited.add((i, j))
        comp = [(i, j)]
        while q:
            x, y = q.pop()
            for X, Y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if (
                    0 <= X < h
                    and 0 <= Y < w
                    and g[X][Y] == 0
                    and (X, Y) not in visited
                ):
                    visited.add((X, Y))
                    q.append((X, Y))
                    comp.append((X, Y))
        return comp

    for i in range(h):
        for j in range(w):
            if g[i][j] == 0 and (i, j) not in visited:
                comp = bfs(i, j)
                n = len(comp)
                color = 3 if n == 1 else 2 if n == 2 else 1
                for x, y in comp:
                    r[x][y] = color
    return r
#Flagged