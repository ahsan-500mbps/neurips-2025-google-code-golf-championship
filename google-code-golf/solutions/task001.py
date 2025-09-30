# In solutions/task001.py
import numpy as n
p=lambda g:n.kron(n.array(g)>0,g).tolist()