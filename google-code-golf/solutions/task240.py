w=None
from collections import*
def с1(grid):
	C=grid;A=len(C);B=len(C[0])if A else 0
	if A<3 or B<3 or(A-1)%2 or(B-1)%2:return
	D=(A-1)//2;E=(B-1)//2;F=[[0]*E for A in range(D)]
	for G in range(1,A,2):
		for H in range(1,B,2):
			I=C[G][H]
			if not I:continue
			J=(G-1)//2;K=(H-1)//2
			for L in{J,D-1-J}:
				for M in{K,E-1-K}:F[L][M]=I
	return F
def с2(coarse):
	D=True;C=False;A=coarse
	if A is w:return
	L=len(A);M=len(A[0]);N=A[0][0];I={}
	for E in range(L):
		for F in range(M):
			G=A[E][F]
			if G==0 or G==N:continue
			B=I.setdefault(G,[0,C,C,C,C]);B[0]+=1
			if E==0:B[1]=D
			if F==0:B[2]=D
			if E==1:B[3]=D
			if F==1:B[4]=D
	H={B:A for(B,A)in I.items()if A[0]>=8}
	if not H:return
	J=[(B,A)for(B,A)in H.items()if A[1]or A[2]]
	if J:return max(J,key=lambda item:(item[1][0],-item[0]))[0]
	K=[(B,A)for(B,A)in H.items()if A[3]or A[4]]
	if K:return max(K,key=lambda item:(item[1][0],-item[0]))[0]
def с3(coarse,edge):
	F=edge;A=coarse
	if A is w:return
	H=len(A);O=len(A[0]);P=Counter(A for B in A for A in B if A);Q=[A for(A,B)in P.items()if B>=8];G=[A[:]for A in A]
	for B in Q:
		for C in range(H):
			I=A[C];D=[A for(A,C)in enumerate(I)if C==B]
			if len(D)<2:continue
			if B==F:
				if not any(A not in(0,F)for A in I):continue
			elif not any(A not in(0,F,B)for A in I):continue
			for(J,K)in zip(D,D[1:]):
				if J==0 and K==O-1:continue
				if any(A[C][B]!=0 for B in range(J+1,K)):continue
				for E in range(J+1,K):
					if G[C][E]==0:G[C][E]=B
		for E in range(O):
			L=[A[B][E]for B in range(H)];D=[A for(A,C)in enumerate(L)if C==B]
			if len(D)<2:continue
			if B==F:
				if not any(A not in(0,F)for A in L):continue
			elif not any(A not in(0,F,B)for A in L):continue
			for(M,N)in zip(D,D[1:]):
				if M==0 and N==H-1:continue
				if any(A[B][E]!=0 for B in range(M+1,N)):continue
				for C in range(M+1,N):
					if G[C][E]==0:G[C][E]=B
	return G
def et(coarse,height,width):
	B=coarse;A=[[0]*width for A in range(height)]
	if B is w:return A
	for(D,E)in enumerate(B):
		for(F,C)in enumerate(E):
			if C:A[2*D+1][2*F+1]=C
	return A
def s9(I):
	A=[list(A)for A in I];C=len(A);D=len(A[0])if C else 0;B=с1(A)
	if B is w:return I
	E=с2(B);F=с3(B,E);G=et(F,C,D);return tuple(tuple(A)for A in G)
def p(g):
	try:
		B=tuple(tuple(A)for A in g);A=s9(B)
		if isinstance(A,tuple):return[list(A)for A in A]
		if isinstance(A,list)and all(isinstance(A,list)for A in A):return A
		return[list(A)for A in g]
	except Exception:return[list(A)for A in g]