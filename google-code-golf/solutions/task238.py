def mc(grid):
	B=grid
	if not B or not B[0]:return 0
	A={}
	for D in B:
		for C in D:A[C]=A.get(C,0)+1
	return max(A,key=A.get)
def o1(grid,u8,da,wb):
	L=u8;A=grid
	if not A or not A[0]:return[]
	M,N=len(A),len(A[0]);O=mc(A)if wb else None;P=[(-1,0),(1,0),(0,-1),(0,1)]
	if da:P+=[(-1,-1),(-1,1),(1,-1),(1,1)]
	D,Q=set(),[]
	for E in range(M):
		for F in range(N):
			if(E,F)in D:continue
			R=A[E][F]
			if R==O:continue
			G,H=set(),[(E,F)]
			while H:
				B,C=H.pop()
				if(B,C)in D:continue
				I=A[B][C]
				if L and I!=R or not L and I==O:continue
				D.add((B,C));G.add((I,(B,C)))
				for(S,T)in P:
					J,K=B+S,C+T
					if 0<=J<M and 0<=K<N and(J,K)not in D:H.append((J,K))
			if G:Q.append(G)
	return Q
def t1(obj):
	A=obj
	if not A:return set()
	B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,B)for(C,(A,B))in A}
	return set(A)
def bb(patch):A=t1(patch);B=min(A for(A,B)in A);C=min(A for(B,A)in A);D=max(A for(A,B)in A);E=max(A for(B,A)in A);return(B,C),(D,E)
def n1(obj):
	A=obj
	if not A:return A
	(B,C),D=bb(A);return{(A,(D-B,E-C))for(A,(D,E))in A}
def s1(patch,d):
	A=patch;C,D=d
	if not A:return A
	B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(B+C,E+D))for(A,(B,E))in A}
	return{(A+C,B+D)for(A,B)in A}
def c2(grid,start,dims):A,B=start;C,D=dims;return[A[B:B+D]for A in grid[A:A+C]]
def s2(patch,grid):(A,B),(C,D)=bb(patch);return c2(grid,(A,B),(C-A+1,D-B+1))
def v1(idx):
	A=t1(idx)
	if not A:return set()
	(B,C),(B,D)=bb(A);E=C+D;return{(A,E-B)for(A,B)in A}
def c3(a,b):
	A,B=a;C,D=b;E,F=min(A,C),min(B,D);G,H=max(A,C),max(B,D)
	if A==C:return{(A,B)for B in range(F,H+1)}
	if B==D:return{(A,B)for A in range(E,G+1)}
	if C-A==D-B:return{(A,B)for(A,B)in zip(range(E,G+1),range(F,H+1))}
	if C-A==B-D:return{(A,B)for(A,B)in zip(range(E,G+1),range(H,F-1,-1))}
	return set()
def p1(grid,obj):
	A=grid;B=len(A);F=len(A[0])if B and A[0]else 0;C=[list(A)for A in A]
	for(G,(D,E))in obj:
		if 0<=D<B and 0<=E<F:C[D][E]=G
	return C
def f2(grid,idx):
	A=grid;B=len(A);F=len(A[0])if B and A[0]else 0;C=[list(A)for A in A]
	for(D,E)in t1(idx):
		if 0<=D<B and 0<=E<F:C[D][E]=8
	return C
def s9(I):
	A=o1(I,u8=False,da=True,wb=True)
	if not A:return I
	G={(8,(A,C))for(A,B)in enumerate(I)for(C,D)in enumerate(B)if D==8};H=lambda o:len(t1(o));J=G or min(A,key=lambda x:len({z for(z,_)in x}));K=[A for A in A if{A for(A,B)in A}!={8}]or A;B=max(K,key=H,default=None)
	if not B:return I
	D={(A,B)for(A,B)in B if A!=8};L=s2(D or B,I);C=t1(s1(n1(J),(1,1)));E=list(n1(D or B));M=p1(L,[(min(E,key=lambda t,i=A,j=B:abs(t[1][0]-i)+abs(t[1][1]-j))[0]if E else 0,(A,B))for(A,B)in C]);(N,O),(P,Q)=bb(C);F=c3((N,O),(P,Q));R=C&(F|v1(F));return f2(M,R)
def p(g):return s9(g)