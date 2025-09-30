def p(j,A=enumerate):
 m=lambda v:[(i,k)for i,r in A(j)for k,x in A(r)if x==v]
 c=m(2);s=m(8)
 if not c or not s:return j
 k=lambda W:(min(i for i,_ in W),max(i for i,_ in W),min(k for _,k in W),max(k for _,k in W))
 l,J,a,C=k(c);e,K,w,L=k(s);b=d=0
 if C<w:d=w-C-1
 elif L<a:d=L-a+1
 elif J<e:b=e-J-1
 elif K<l:b=K-l+1
 f,g={*c},{*s}
 return[[8 if(i,k)in g else 2 if(i-b,k-d)in f else 0 for k,_ in A(j[0])]for i,_ in A(j)]
