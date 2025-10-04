#TODO  # TO BE DONE BY Suhrid Sadman Abrar
def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 Z=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] #3x3
 P=[[0,0],[0,1],[1,0],[1,1]] #2x2
 Q=[[0,0],[0,1],[0,2]] #1x3
 S=[[0,0],[1,0],[2,0]] #3x1
 for r in R(h):
  for c in R(w):
   try:
    if [g[r+i[0]][c+i[1]] for i in Z]==[5,5,5,5,5,5,0,0,5]:
     Y=[8,8,2,8,8,2,0,0,2]
     for i in R(L(Z)): 
      g[r+Z[i][0]][c+Z[i][1]]=Y[i]
    elif [g[r+i[0]][c+i[1]] for i in Z]==[5,5,5,5,5,5,5,0,0]:
     Y=[2,8,8,2,8,8,2,0,0]
     for i in R(L(Z)): 
      g[r+Z[i][0]][c+Z[i][1]]=Y[i]
    elif [g[r+i[0]][c+i[1]] for i in Z]==[0,5,5,0,5,5,5,5,5]:
     Y=[0,8,8,0,8,8,2,2,2]
     for i in R(L(Z)): 
      g[r+Z[i][0]][c+Z[i][1]]=Y[i]
    elif [g[r+i[0]][c+i[1]] for i in Z]==[5,5,5,5,5,0,5,5,0]:
     Y=[2,2,2,8,8,0,8,8,0]
     for i in R(L(Z)): 
      g[r+Z[i][0]][c+Z[i][1]]=Y[i]
   except: pass
 for r in R(h):
  for c in R(w):
   try:
    if [g[r+i[0]][c+i[1]] for i in P]==[5,5,5,5]:
     for i in P: 
      g[r+i[0]][c+i[1]]=8
    elif [g[r+i[0]][c+i[1]] for i in Q]==[5,5,5]:
     for i in Q: 
      g[r+i[0]][c+i[1]]=2
    elif [g[r+i[0]][c+i[1]] for i in S]==[5,5,5]:
     for i in S: 
      g[r+i[0]][c+i[1]]=2
   except: pass
 return g
#FLAGGED