def p(g):
 R=range;h=len(g);w=len(g[0])
 d={(i+j)%3:g[i][j]for i in R(h)for j in R(w)if g[i][j]}
 return[[d.get((i+j)%3,0)for j in R(w)]for i in R(h)]