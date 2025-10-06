# TODO  # TO BE DONE BY Suhrid Sadman Abrar
from math import gcd

def p(g):
    for r in g:
        I=[i for i,v in enumerate(r) if v==8]
        if not I: 
            continue
        last=I[-1]
        if last==len(r)-1:
            continue
        # infer pattern period from gaps between 8s (contiguous -> 1, alternating -> 2, etc.)
        d=0
        for a,b in zip(I,I[1:]): d=gcd(d,b-a)
        per=d or 1
        phase=I[0]%per if per>1 else 0
        for j in range(last+1,len(r)):
            r[j]=1 if (per==1 or j%per==phase) else 0
    return g
#FLAGGED
