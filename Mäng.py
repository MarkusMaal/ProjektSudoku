from random import randint

# loogika testimine
arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rida = []
read = []
for i in range(9):
    arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rida = []
    for i in range(9):
        valik = randint(0, len(arvud) - 1)
        good = False
        while not good:
            if len(read) - 1 >= i:
                # kontrolli arve horisontaalselt
                for x in range(len(read[i])):
                    good = True
                    if read[i][x] == valik:
                        valik = randint(0, len(arvud) - 1)
                        good = False
                        break
            # kontrolli arve vertikaalselt
            for j in range(len(read)):
                good = True
                if read[j][i] == valik:
                    valik = randint(0, len(arvud) - 1)
                    good = False
                    break
            if len(read) == 0:
                good = True
                break
        rida.append(arvud[valik])
        del arvud[valik]
    read.append(rida)
for rida in read:
    print(rida)
