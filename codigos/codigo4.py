from os.path import exists
import re
archive_name1 = "/content/drive/MyDrive/tcc/e1 B2 scopus 1368.bib"
archive_name = "/content/drive/MyDrive/tcc/e1 B2 wos 1086.txt"
l1 = []
l2 = []
if exists(archive_name1):
    with open(archive_name1, "r") as arq:
        msg = arq.read().splitlines()
    for m in msg:
        if "title" in m:
            patern = re.compile("(title={)|(},?)")
            t = patern.sub("", m)
            if not t in l1:
                l1.append(t)
if exists(archive_name2):
    with open(archive_name2, "r") as arq:
        msg = arq.read().splitlines()
    for m in msg:
        if "TI " in m:
            t = m.replace("TI ", "")
            if not t in l2:
                l2.append(t)
