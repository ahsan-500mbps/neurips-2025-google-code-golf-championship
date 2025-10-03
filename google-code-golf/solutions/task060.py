#TODO # TO BE DONE BY AHSAN TARIQ
def p(g):
    H,W=len(g),len(g[0]); m=W//2
    out=[[0]*W for _ in range(H)]
    for i,row in enumerate(g):
        nz=[j for j,x in enumerate(row) if x]   # nonzero positions
        if len(nz)>=2:
            L=row[nz[0]]; R=row[nz[-1]]
            out[i]=[L]*m+[5]+[R]*(W-m-1)
    return out
