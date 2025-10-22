def p(g,E=enumerate):
 Z={i for i,c in E(zip(*g))if 2 in c}
 return[[1 if 1 in r else 3 if 3 in r else 2 if(not v and c in Z)else v for c,v in E(r)]for r in g]
