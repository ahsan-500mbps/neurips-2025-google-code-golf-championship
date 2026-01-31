def p(g):
    h, w = len(g), len(g[0])
    flat = sum(g, [])
    bg = max(set(flat), key=flat.count)
    o = [r[:] for r in g]

    # horizontal propagation
    for i in range(h):
        c = bg
        for j in range(w):
            if g[i][j] != bg:
                c = g[i][j]
            o[i][j] = c
        c = bg
        for j in range(w - 1, -1, -1):
            if g[i][j] != bg:
                c = g[i][j]
            o[i][j] = c if o[i][j] == bg else o[i][j]

    # vertical propagation
    for j in range(w):
        c = bg
        for i in range(h):
            if g[i][j] != bg:
                c = g[i][j]
            o[i][j] = c if o[i][j] == bg else o[i][j]
        c = bg
        for i in range(h - 1, -1, -1):
            if g[i][j] != bg:
                c = g[i][j]
            o[i][j] = c if o[i][j] == bg else o[i][j]

    return o