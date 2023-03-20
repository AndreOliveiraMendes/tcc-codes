from os.path import exists
archive_name1 = "/content/drive/MyDrive/tcc/e1 B2 wos 1086.txt"
archive_name2 = "/content/drive/MyDrive/tcc/e1 B2 scopus 1368.bib"
msg1, msg2 = [], []
print(archive_name1)
if exists(archive_name1):
    with open(archive_name1, "r") as arq:
        msg1 = arq.read().splitlines()
else:
    print("arquivo 1 não existe ou não pode ser lido")
if exists(archive_name2):
    with open(archive_name2, "r") as arq:
        msg2 = arq.read().splitlines()
else:
    print("arquivo 2 não existe ou não pode ser lido")
if msg1:
    for m in msg1:
        print(m)
if msg2:
    for m in msg2:
        print(m)
