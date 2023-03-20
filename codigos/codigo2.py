import re
archive_name = "/content/drive/MyDrive/tcc/e1 B2 scopus 1368.bib"
l1 = []
if exists(archive_name):
    with open(archive_name, "r") as arq:
        msg = arq.read().splitlines()
    for m in msg:
        if "title" in m:
            patern = re.compile("(title={)|(},?)")
            t = patern.sub("", m)
            l1.append(t)
            print(l1)
