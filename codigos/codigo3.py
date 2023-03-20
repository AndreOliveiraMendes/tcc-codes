from os.path import exists
archive_name = "/content/drive/MyDrive/tcc/e1 B2 wos 1086.txt"
l2 = []
if exists(archive_name):
    with open(archive_name, "r") as arq:
        msg = arq.read().splitlines()
    for m in msg:
        if "TI " in m:
            t = m.replace("TI ", "")
            print(t)
            l2.append(t)
