max_sep = len(l1)
dist = 0
for n, t in enumerate(l1):
    if t in l2:
        dist += abs(n - l2.index(t))
    else:
        dist += max_sep
grau_sep = dist/(max_sep*max_sep)
grau_sim = 1 - grau_sep
print(100*grau_sep)
print(100*grau_sim)
