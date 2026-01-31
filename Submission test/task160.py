import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

p=lambda g:[[2 if flip(g,1)[y][x]==1 and g[y][x]==0 else g[y][x] for x in range(len(g[0]))]for y in range(len(g))]

#Flagged