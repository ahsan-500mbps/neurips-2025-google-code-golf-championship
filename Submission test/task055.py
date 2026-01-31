def p(j):
 c,E=len(j),len(j[0]);k=[r[:]for r in j];W,l=[i for i in range(c)if all(x==8 for x in j[i])];J,a=[i for i in range(E)if all(r[i]==8 for r in j)]
 for C in range(c):
  for e in range(E):
   if not k[C][e]:
    if C<W and J<e<a:k[C][e]=2
    elif W<C<l and e<J:k[C][e]=4
    elif W<C<l and J<e<a:k[C][e]=6
    elif W<C<l and e>a:k[C][e]=3
    elif C>l and J<e<a:k[C][e]=1
 return k