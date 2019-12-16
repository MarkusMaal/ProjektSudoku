from random import randint




# loogika testimine
arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]

blokk = []
# üks rida muutujas tabel tähistab ühte gruppi
# tärn on grupi eraldaja
# ... on ühe rea gruppe eraldaja
tabel = "521 467 000*" \
        "000 000 000*" \
        "000 000 000*" \
        "..." \
        "000 000 000*" \
        "000 000 000*" \
        "000 000 000*" \
        "..." \
        "000 000 000*" \
        "000 000 000*" \
        "000 000 000*"

clusterid = tabel.split("...")


read = []
rida = []


def CreateSection(count, arvud, empties, eelmine, ülemine):
    s = ""
    eelread = eelmine.split("\n")
    üleread = ülemine.split("\n")
    ülekolonnid = []
    for i in range(3):
        ülekolonnid.append(üleread[0][i] + üleread[1][i] + üleread[2][i])
    rida = 1
    for i in range(empties):
        arvud.append(0)
    for i in range(count):
        if len(s) > 3: s = ""
        teststring = eelread[0]
        test = randint(0, len(arvud) - 1)
        while (teststring in eelread[rida - 1]) or (teststring in ülekolonnid[rida - 1]):
            test = randint(0, len(arvud) - 1)
            teststring = str(arvud[test])
            print(teststring)
        s += teststring
        arvud.remove(arvud[test])
        if i == 2 or i == 5:
            rida += 1
            s += "\n"
    return s

def CheckBlock(location, clusterid):
    isin = False
    ly = 1
    for cluster in clusterid:
        for group in cluster.split("*"):
            print(group)

clusterid = []
eelmine = "000\n000\n000"
for d in range(3):
    sektsioonid = []
    for i in range(3):
        if d == 0:
            ülemine = "000\n000\n000"
        else:
            ülemine = clusterid[-1][i]
        sektsioonid.append(CreateSection(9, arvud, 4, eelmine, ülemine))
        eelmine = sektsioonid[-1]
        arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    clusterid.append(sektsioonid)
print(clusterid)
