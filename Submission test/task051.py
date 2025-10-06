def p(g):
 from collections import Counter
 h,w=len(g),len(g[0]);s=min((v for r in g for v in r if v),key=lambda x:Counter(v for r in g for v in r if v)[x])
 i,j=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==s][0];u=g[i-1][j]if i else 0;d=g[i+1][j]if i<h-1 else 0;l=g[i][j-1]if j else 0;r=g[i][j+1]if j<w-1 else 0
 di,dj=(1,0)if u==0<d else(-1,0)if d==0<u else(0,1)if l==0<r else(0,-1)if r==0<l else(-1,0)
 while 0<=i+di<h and 0<=j+dj<w:i+=di;j+=dj;g[i][j]=g[i][j]or s
 return g
