T=lambda a:[list(r)for r in zip(*a)]
def p(a):
 def f():
  h,w=len(a),len(a[0])
  for y in range(h):
   for x in range(w-1):
    if a[y][x]==a[y][x+1]==2:
     for Y in range(max(0,y-1),min(h,y+2)):
      for X in range(max(0,x-1),min(w,x+3)):
       if a[Y][X]-2:a[Y][X]=3
 f();a=T(a);f();return T(a)