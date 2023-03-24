import pandas as pd
#gerando os arquivos em txt
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
#gerando os arquivo em excel
df1 = pd.DataFrame({'posição': list(range(1, len(l1) + 1)),
                    'Titulo': l1})
df2 = pd.DataFrame({'posição': list(range(1, len(l2) + 1)),
                    'Titulo': l2})
writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='titulos do arquivo.bib', index=False)
df2.to_excel(writer, sheet_name='titulos do arquivo.txt', index=False)
writer.close()
