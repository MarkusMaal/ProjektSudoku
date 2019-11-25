from random import randint

# loogika testimine
arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]

blokk = []
blokid = []


read = []
rida = []


def CheckBlock(x, blokid):
    isin = False
    for b in blokid:
        for subb in b:
            if subb == x:
                isin = True
    return isin


def CheckGrid(kontroll, valik, positsioon):
    # vali välja millist rida kontrollida
    y = positsioon[1]
    complist = kontroll[y]
    print(complist)
    tagasta = False
    for item in complist:
        if item == valik:
            tagasta = True
    return tagasta

# sektsioonidesse lisatakse 3x3 2d listidena


sektsioonid = []

print("Sudoku backend test")

for i in range(3):
    if i == 3 or i == 6: arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in range(3):
        blokk = []
        while len(blokk) < 3:
            if len(arvud) == 0:
                break
            e = randint(0, len(arvud) - 1)
            valik = arvud[e]
            blokk.append(valik)
            arvud.remove(valik)
        blokid.append(blokk)

"""for h in range(9):
    rida.append(arvud[valik])
    del arvud[valik]
    read.append(rida)"""
uusb = []
for b in blokid:
    if not b == []:
        uusb.append(b)
sektsioonid.append(uusb)

for x in range(2):
    kontroll = sektsioonid[-1]
    fails = 0
    arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        test = 0
        for d in range(3):
            blokk = []
            while len(blokk) < 3:
                if len(arvud) == 0:
                    break
                e = test
                if len(arvud) - 1 >= e:
                    valik = arvud[e]
                if fails > len(arvud):
                    fails = 0
                    valik = 0
                if CheckGrid(kontroll, valik, [d, i]):
                    test += 1
                    if test > len(arvud) - 1:
                        test = 0
                        fails += 1
                    continue
                else:
                    if len(arvud) == 0:
                        break
                    else:
                        blokk.append(valik)
                        if valik in arvud: arvud.remove(valik)
            blokid.append(blokk)

    """for h in range(9):
        rida.append(arvud[valik])
        del arvud[valik]
        read.append(rida)"""
    uusb = []
    for b in blokid:
        if not b == []:
            if not b in sektsioonid[-1]:
                uusb.append(b)
    sektsioonid.append(uusb)
print(sektsioonid)
