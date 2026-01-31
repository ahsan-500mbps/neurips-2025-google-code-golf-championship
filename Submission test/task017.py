def p(j, R=range, L=len, E=enumerate):
 f = lambda x, y: x == y or x * y < 1
 W, H = L(j[0]), L(j)
 J = next((s for s in R(1, W) if all(f(a, b) for r in j for a, b in zip(r, r[s:]))), W)
 A = next((s for s in R(1, H) if all(f(a, b) for r1, r2 in zip(j, j[s:]) for a, b in zip(r1, r2))), H)
 C = {(i % A, k % J): v for i, r in E(j) for k, v in E(r) if v}
 [r.__setitem__(k, C[i % A, k % J]) for i, r in E(j) for k, v in E(r) if not v]
 return j
