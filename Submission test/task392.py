L=len;R=range
def p(g):
 h,w=L(g),L(g[0]);F=[v for r in g for v in r];b=5;S=[v for v in set(F)if v];C=S[0] if S else b
 rs=[sum(v==C for v in g[i])%2 for i in R(h)]
 cs=[sum(g[i][j]==C for i in R(h))%2 for j in R(w)]
 for i in R(h-2,-1,-1):rs[i]^=rs[i+1]
 for j in R(1,w):cs[j]^=cs[j-1]
 return [[C if rs[i] or cs[j] else b for j in R(w)]for i in R(h)]
#FLAGGED