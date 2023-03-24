first = True
with open("resultado1.txt", "w") as arq:
    for t in l1:
        if first:
            first = False
        else:
            arq.write("\n")
        arq.write(t)
first = True
with open("resultado2.txt", "w") as arq:
    for t in l2:
        if first:
            first = False
        else:
            arq.write("\n")
        arq.write(t)
