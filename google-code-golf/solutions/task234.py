def p(g):
    R=range; L=len
    h,w=L(g),L(g[0])
    cols=sorted({v for r in g for v in r if v})
    if not cols: return g
    def bbox(c):
        rs=[i for i in R(h) if any(x==c for x in g[i])]
        if not rs: return None
        cs=[j for j in R(w) if any(g[i][j]==c for i in R(h))]
        return min(rs),max(rs),min(cs),max(cs)
    bxs={c:bbox(c) for c in cols}
    ctr=lambda b:((b[0]+b[1])/2,(b[2]+b[3])/2) if b else (0,0)
    allc=(sum(i for i,r in enumerate(g) for _ in r if _),
          sum(j for r in g for j,v in enumerate(r) if v))
    nz=sum(1 for r in g for v in r if v) or 1
    global_ctr=(allc[0]/nz, allc[1]/nz)
    out=[r[:] for r in g]

    for c in cols:
        b=bxs[c]
        if not b: continue
        r0,r1,c0,c1=b
        H,W=r1-r0+1,c1-c0+1
        keep=[[0]*W for _ in R(H)]
        for i in R(r0,r1+1):
            for j in R(c0,c1+1):
                if g[i][j]==c:
                    hv = (j>c0   and g[i][j-1]==c) or (j<c1 and g[i][j+1]==c)
                    vv = (i>r0   and g[i-1][j]==c) or (i<r1 and g[i+1][j]==c)
                    if hv and vv: keep[i-r0][j-c0]=1
        if not any(any(row) for row in keep): continue
        if L(cols)==2:
            other=cols[0] if cols[1]==c else cols[1]
            oc=bxs[other]
            ty,tx=ctr(oc)
        else:
            ty,tx=global_ctr
        cy,cx=ctr(b)
        dy,dx=ty-cy, tx-cx
     
        if abs(dy)>=abs(dx):   
            if dy<0: 
                top=0
                while top<H and not any(keep[top]): top+=1
                if top:
                    keep=keep[top:]+[[0]*W for _ in R(top)]
            else:     
                bot=0
                while bot<H and not any(keep[H-1-bot]): bot+=1
                if bot:
                    keep=[[0]*W for _ in R(bot)] + keep[:H-bot]
        else:
            def col_empty(j): return not any(keep[i][j] for i in R(H))
            if dx<0:  
                left=0
                while left<W and col_empty(left): left+=1
                if left:
                    keep=[row[left:]+[0]*left for row in keep]
            else:     
                right=0
                while right<W and col_empty(W-1-right): right+=1
                if right:
                    keep=[[0]*right+row[:W-right] for row in keep]
        for i in R(r0,r1+1):
            for j in R(c0,c1+1):
                if out[i][j]==c: out[i][j]=0
        for i in R(H):
            for j in R(W):
                if keep[i][j]: out[r0+i][c0+j]=c

    return out
