from collections import *
p=lambda j:(lambda c:(lambda r:(lambda E:(lambda m,M:[k[m:M+1]for k in r])(min(E),max(E)))([i for k in r for i,x in enumerate(k)if x==c]))([k for k in j if c in k]))([v for v,_ in Counter(sum(j,[])).most_common(3)if v>0][-1])
