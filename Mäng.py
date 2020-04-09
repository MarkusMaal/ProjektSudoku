from tkinter import *
from tkinter import font
from random import *
import time


# klass, milles üks objekt on 1 ruut
class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    # joonistab ruudu ja sisse numbri
    def DrawCell(self):
        self.joonis = tahvel.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill="white", outline="black", width=1, activefill="lightblue")
        self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value))
        tahvel.tag_bind(self.joonis, '<1>', self.clicked)
        tahvel.tag_bind(self.number, '<1>', self.clicked)

    # määrab numbri, mis cell'i/ruudu eelnevale numbrile asemele panna
    def keypress(self, event=None):
        if int(event.char) > 0 and int(event.char) < 10:
            self.value = event.char
            cell_grid[self.y // 55][self.x // 55] = event.char
            print("Vertikaalne: " + str(KontrolliVertikaalrida(cell_grid, self.x // 55)))
            print("Horisontaalne: " + str(KontrolliHorisontaalrida(cell_grid, self.y // 55)))
            print("Sisemine: " + str(KontrolliSisemist(cell_grid, LeiaSuurKast(self.x // 55, self.y // 55))))
            tahvel.delete(self.number)
            tahvel.delete(self.joonis)
            Cell.DrawCell(self)

    # teeb koha "..."'iks, ootab sisendit kasutajalt
    def clicked(self, event=None):
        tahvel.delete(self.number)
        self.number = tahvel.create_text(self.x + 25, self.y + 25, text="...")
        tahvel.tag_bind(self.number, '<1>', self.clicked)
        raam.bind("<Key>", self.keypress)

# veerg - kontrollitav veerg
# int_cells - kõik listid argumendina
# märgid - leitud märgid reast
# duplikaate - kui True, leiti mitu ühesugust numbrit


def KontrolliVertikaalrida(int_cells, veerg , nulliga = False):
    märgid = []
    duplikaate = False
    kontroll_list = []
    for i in range(9):
        kontroll_list.append(int_cells[i][veerg])
    for i in range(9):
        if nulliga:
            if not str(kontroll_list[i]) in märgid:
                märgid.append(str(kontroll_list[i]))
            else:
                duplikaate = True
        else:
            if not str(kontroll_list[i]) == "0":
                if not str(kontroll_list[i]) in märgid:
                    märgid.append( str(kontroll_list[i]))
                else:
                    duplikaate = True
    print(kontroll_list, duplikaate)
    return duplikaate


raam = Tk()
raam.title("Sudoku")
raam.geometry("700x500")

tahvel = Canvas(raam, width=500, height=500, background="white")
tahvel.grid()

cell_grid = []
for i in range(9):
    one_grid = []
    for i in range(9):
        arv = 0
        one_grid.append(arv)
    cell_grid.append(one_grid)
read = []
rida = []
# joonistab paksemad jooned


def DrawLines():
    tahvel.create_rectangle(0, 0, 500, 500, fill="black")
    tahvel.create_line(0, 163, 500, 163, width=3, fill="white")
    tahvel.create_line(0, 328, 500, 328, width=3, fill="white")
    tahvel.create_line(163, 0, 163, 500, width=3, fill="white")
    tahvel.create_line(328, 0, 328, 500, width=3, fill="white")


def NewGame():
    cell_grid = []
    for i in range(9):
        one_grid = []
        for j in range(9):
            arv = 0
            one_grid.append(arv)
        cell_grid.append(one_grid)
    # üleval vasak
    jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = -1
    offset = 0
    for i in range(9):
        if i % 3 == 0:
            row += 1
        r1 = randint(0, len(jupid) - 1)
        cell_grid[row][offset + i - (row * 3)] = jupid[r1]
        jupid.remove(jupid[r1])
    fine = False
    while not fine:
        # üleval keskmine
        jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        row = -1
        offset = 3
        for i in range(9):
            if i % 3 == 0:
                row += 1
            r1 = randint(0, len(jupid) - 1)
            cell_grid[row][offset + i - (row * 3)] = jupid[r1]
            cycles = 0
            fine = True
            while KontrolliHorisontaalrida(cell_grid, row):
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                cell_grid[row][offset + i - (row * 3)] = jupid[r1]
                cycles += 1
                if cycles == 10:
                    fine = False
                    break
            jupid.remove(jupid[r1])
    # keskmine
    fine = False
    while not fine:
        jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        row = 2
        offset = 3
        for i in range(9):
            if i % 3 == 0:
                row += 1
            r1 = randint(0, len(jupid) - 1)
            cell_grid[row][offset + i - (row * 3)] = jupid[r1]
            cycles = 0
            fine = True
            while KontrolliVertikaalrida(cell_grid, offset + i - (row * 3)):
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                cell_grid[row][offset + i - (row * 3)] = jupid[r1]
                cycles += 1
                if cycles == 10:
                    fine = False
                    break
            jupid.remove(jupid[r1])

    # keskmine parem
    fine = False
    while not fine:
        jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        row = 2
        offset = 6
        for i in range(9):
            if i % 3 == 0:
                row += 1
            r1 = randint(0, len(jupid) - 1)
            cell_grid[row][offset + i - (row * 3)] = jupid[r1]
            cycles = 0
            fine = True
            while KontrolliHorisontaalrida(cell_grid, row):
                if cycles == 10:
                    fine = False
                    break
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                cell_grid[row][offset + i - (row * 3)] = jupid[r1]
                cycles += 1
            jupid.remove(jupid[r1])

    # see koodujupp eemaldab teatud numbrid kastidest
    # kuni kaks korda
    for i in range(2):
        for j in range(9):
            r1 = randint(0, 8)
            cell_grid[j][r1] = 0
    cells = []
    for i in range(0, 9):
        for j in range(0, 9):
            outpt = str(cell_grid[i][j]).replace("0", " ")
            cell = Cell(j * 55, i * 55, outpt)
            cells.append(cell)
    DrawLines()
    for cell in cells:
        cell.DrawCell()


def CheckBtn():
    currentstate = True
    for i in range(1, 9, 1):
        if KontrolliSisemist(cell_grid, i, False): currentstate = False
        if KontrolliVertikaalrida(cell_grid, i, False): currentstate = False
        if KontrolliHorisontaalrida(cell_grid, i, False): currentstate = False
    print(currentstate)


# kontrollib horistonaalset rida


def KontrolliHorisontaalrida(int_cells, rida, nulliga = False):
    märgid = []
    duplikaate = False
    kontroll_check = int_cells[rida]
    for i in range(9):
        if nulliga:
            if not str(kontroll_check[i]) in märgid:
                märgid.append(str(kontroll_check[i]))
            else:
                duplikaate = True
        else:
            if not str(kontroll_check[i]) == "0":
                if not str(kontroll_check[i]) in märgid:
                    märgid.append(str(kontroll_check[i]))
                else:
                    duplikaate = True
    return duplikaate


# leiab suure kasti vastavalt väikse kasti koordinaatidele

def LeiaSuurKast(x, y):
    if x < 3:
        if y < 3:
            return 1
        elif 3 <= y < 6:
            return 4
        else:
            return 7
    elif 3 <= x < 6:
        if y < 3:
            return 2
        elif 3 <= y < 6:
            return 5
        else:
            return 8
    else:
        if y < 3:
            return 3
        elif 3 <= y < 6:
            return 6
        else:
            return 9


def KontrolliSisemist(int_cells, kast, nulliga = False):
    märgid = []
    duplikaate = False
    if kast == 1:
        offset_x = 0
        offset_y = 0
    elif kast == 2:
        offset_x = 3
        offset_y = 0
    elif kast == 3:
        offset_x = 6
        offset_y = 0
    elif kast == 4:
        offset_x = 0
        offset_y = 3
    elif kast == 5:
        offset_x = 3
        offset_y = 3
    elif kast == 6:
        offset_x = 6
        offset_y = 3
    elif kast == 7:
        offset_x = 0
        offset_y = 6
    elif kast == 8:
        offset_x = 3
        offset_y = 6
    elif kast == 9:
        offset_x = 6
        offset_y = 6
    for i in range(3):
        for j in range(3):
            if nulliga:
                if not int_cells[offset_y + i][offset_x + j] in märgid:
                    märgid.append(int_cells[offset_y + i][offset_x + j])
                else:
                    duplikaate = True
            else:
                if not int_cells[offset_y + i][offset_x + j] == 0:
                    if not int_cells[offset_y + i][offset_x + j] in märgid:
                        märgid.append(int_cells[offset_y + i][offset_x + j])
                    else:
                        duplikaate = True
    return duplikaate


# joonistab ruudustiku
def Draw():
    DrawLines()
    uus_mäng = Button(raam, text="Uus mäng", command=NewGame)
    uus_mäng.grid(row=0, column=1)
    for i in cells:
        Cell.DrawCell(i)
    kontrolli = Button(raam, text="Kontrolli", command=CheckBtn)
    kontrolli.grid(row=0, column=2)


cells = []


# loob Cell() objektid
for i in range(0, 9):
    for j in range(0, 9):
        outpt = str(cell_grid[i][j]).replace("0", " ")
        cell = Cell(j*55, i*55, outpt)
        cells.append(cell)


Draw()

raam.mainloop()

"""

# kood, mis pole hetkel kasutusel, kuid mida võib kunagi vaja minna...

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
    arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rida1[i].Defineeri(CreateSection(9, arvud, 3))
print(rida1[0].Kontrolli(0, 0, 5))
"""