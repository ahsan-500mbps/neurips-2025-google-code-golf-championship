def p(a):
    h,w=len(a),len(a[0]);m={}
    for i in range(h):
        for j in range(w):
            v=a[i][j]
            if v:m.setdefault(v,[0,0,0]);m[v][0]+=i;m[v][1]+=j;m[v][2]+=1
    c=[(s/k,t/k,v)for v,(s,t,k) in m.items() if k]
    c.sort(key=lambda x:x[0]);u=sorted(c[:2],key=lambda x:x[1]);d=sorted(c[2:],key=lambda x:x[1])
    tl,tr,bl,br=u[0][2],u[1][2],d[0][2],d[1][2]
    b=[[0]*4 for _ in range(4)]
    for i in (0,1): b[i][0]=b[i][1]=tl; b[i][2]=b[i][3]=tr
    for i in (2,3): b[i][0]=b[i][1]=bl; b[i][2]=b[i][3]=br
    return b