def get_grau(l1, l2, top):
    lenght = min(len(l1), len(l2))
    dist = 0
    lt1, lt2 = [], []
    if top != "":
        lt = int(top)
        if lt > lenght:
            print("elementos não sulficientes, truncando para o tamanho da menor lista")
        lenght = min(lenght, lt)
    lt1 = l1[:lenght]
    lt2 = l2[:lenght]
    max_sep = lenght
    for n, t in enumerate(lt1):
        if t in lt2:
            dist += abs(n - lt2.index(t))
        else:
            dist += max_sep
    grau_sep = dist/(max_sep*lenght)
    grau_sim = 1 - grau_sep
    return grau_sep, grau_sim, lenght
