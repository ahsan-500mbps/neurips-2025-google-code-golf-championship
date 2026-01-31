def p(g,L=len,Z=zip):
 t=list(Z(*g))
 F=lambda a:(lambda s:next(iter(s-{0}),0))(set(a))
 rr=[F(r)for r in g]
 cc=[F(c)for c in t]
 R=[x for i,x in enumerate(rr)if i<1 or x!=rr[i-1]]
 C=[x for i,x in enumerate(cc)if i<1 or x!=cc[i-1]]
 from collections import Counter
 d=Counter(R+C).most_common(1)[0][0]
 a=next((x for x in R+C if x!=d),d)
 h,w=L(R),L(C)
 return[[d if R[i]==d and C[j]==d else a for j in range(w)]for i in range(h)]
#FLAGGED