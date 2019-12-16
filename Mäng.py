from random import randint

class Grid:
    def __init__(self, rida1 = "000", rida2 = "000", rida3 = "000", veerg1 = "000", veerg2 = "000", veerg3 = "000"):
        self.rida1 = rida1
        self.rida2 = rida2
        self.rida3 = rida3
        self.veerg1 = veerg1
        self.veerg2 = veerg2
        self.veerg3 = veerg3

    def DefineeriVeerud(self):
        self.veerg1 = self.rida1[0] + self.rida2[0] + self.rida3[0]
        self.veerg2 = self.rida1[1] + self.rida2[1] + self.rida3[1]
        self.veerg3 = self.rida1[2] + self.rida2[2] + self.rida3[2]

    def Kontrolli(self, rida, veerg, arv):
        if veerg == 0:
            if rida == 0:
                if str(arv) in self.rida1:
                    return False
                else:
                    return True
            elif rida == 1:
                if str(arv) in self.rida2:
                    return False
                else:
                    return True
            elif rida == 2:
                if str(arv) in self.rida3:
                    return False
                else:
                    return True
        elif veerg > 0:
            if str(arv) in self.veerg1:
                return False
            elif str(arv) in self.veerg2:
                return False
            elif str(arv) in self.veerg3:
                return False
            else:
                return True

    def Defineeri(self, sektsioon):
        self.rida1 = sektsioon.split("\n")[0]
        self.rida2 = sektsioon.split("\n")[1]
        self.rida3 = sektsioon.split("\n")[2]
        self.DefineeriVeerud()

    def ToString(self):
        print(str(self.rida1) + "\n" + str(self.rida2) + "\n" + str(self.rida3))


# loogika testimine
arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]

blokk = []
# üks rida muutujas tabel tähistab ühte gruppi
# tärn on grupi eraldaja
# ... on ühe rea gruppe eraldaja

read = []
rida = []


def CreateSection(count, arvud, empties, eelmine = "000\n000\n000", ülemine = "000\n000\n000"):
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
        # paranda ühte probleemi
        checks = s.split("\n")
        nchecks = ""
        for check in checks:
            e = check
            if len(e) > 3:
                e = e[:3]
            nchecks += e
        teststring = eelread[0]

        test = randint(0, len(arvud) - 1)
        while (teststring in eelread[rida - 1]) or (teststring in ülekolonnid[rida - 1]):
            test = randint(0, len(arvud) - 1)
            teststring = str(arvud[test])
        s += teststring
        arvud.remove(arvud[test])
        if i == 2 or i == 5:
            rida += 1
            s += "\n"
    return s


rida1 = [Grid(), Grid(), Grid()]
for i in range(3):
    rida1[i].Defineeri(CreateSection(9, arvud, 3))
    rida1[i].ToString()
print(rida1[0].Kontrolli(0, 0, 5))
