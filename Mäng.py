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


for i in range(9):
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
print("Sudoku backend test")
uusb = []
for b in blokid:
    if not b == []:
        uusb.append(b)
print(uusb)