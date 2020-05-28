from tkinter import *
from tkinter import font
from tkinter import messagebox
from random import *
import time


# Sudoku projekt
# klass, milles üks objekt on 1 ruut


# Loo väli näidise põhjal
# Muuda seda muutujat, et näidist kasutada/mitte kasutada
kasuta_näidist = False
näidis = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
solved_grid = []

class Cell:
    def __init__(self, x, y, value, protected, cell_grid):
        self.x = x
        self.y = y
        self.value = value
        self.protected = protected
        self.cell_grid = cell_grid

    # joonistab ruudu ja sisse numbri
    def DrawCell(self):
        textcol = "black"
        #else:
        #    textcol = "black"
        if KontrolliVertikaalrida(self.cell_grid, self.x // 55) or KontrolliHorisontaalrida(self.cell_grid, self.y // 55) or KontrolliSisemist(self.cell_grid, LeiaSuurKast(self.x // 55, self.y // 55)):
            textcol = "red"
        self.joonis = tahvel.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill="white", outline="black",
                                              width=1, activefill="lightblue")
        if not self.protected:
            if self.value == "0":
                self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), fill="white")
            else:
                self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), fill=textcol)
        else:
            if self.value == "0":
                self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), font='Arial 12 bold', fill="white")
            else:
                self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), font='Arial 12 bold', fill="black")
        tahvel.tag_bind(self.joonis, '<1>', self.clicked)
        tahvel.tag_bind(self.number, '<1>', self.clicked)

    # 1)määrab numbri, mis cell'i/ruudu eelnevale numbrile asemele panna
    # 2)hoolitseb klahvidega liikumise eest
    def keypress(self, event):
        try:
            if not self.protected:
                if 0 <= int(event.char) < 10:
                    if not int(event.char) == 0:
                        self.value = event.char
                    else:
                        self.value = "0"
                    if not self.value == "0":
                        self.cell_grid[self.y // 55][self.x // 55] = event.char
                        cell_grid[self.y // 55][self.x // 55] = self.value
                    #print("Vertikaalne: " + str(KontrolliVertikaalrida(self.cell_grid, self.x // 55)))
                    #print("Horisontaalne: " + str(KontrolliHorisontaalrida(self.cell_grid, self.y // 55)))
                    #print("Sisemine: " + str(KontrolliSisemist(self.cell_grid, LeiaSuurKast(self.x // 55, self.y // 55))))
                    tahvel.delete(self.number)
                    tahvel.delete(self.joonis)
                    Cell.DrawCell(self)
        # kui vajutatud klahv ei ole number, siis testib, kas on üks nooltest ja läheb sealt edasi
        except ValueError:
            if event.keysym == "Up":
                for i in cells:
                    if i.x == self.x and i.y == self.y - 55:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
            if event.keysym == "Down":
                for i in cells:
                    if i.x == self.x and i.y == self.y + 55:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
            if event.keysym == "Left":
                for i in cells:
                    if i.x == self.x - 55 and i.y == self.y:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
            if event.keysym == "Right":
                for i in cells:
                    if i.x == self.x + 55 and i.y == self.y:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        print(self.value)
                        Cell.arrow_move(i)
        if self.protected:
            if event.keysym == "Up":
                for i in cells:
                    if i.x == self.x and i.y == self.y - 55:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
            if event.keysym == "Down":
                for i in cells:
                    if i.x == self.x and i.y == self.y + 55:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
            if event.keysym == "Left":
                for i in cells:
                    if i.x == self.x - 55 and i.y == self.y:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
            if event.keysym == "Right":
                for i in cells:
                    if i.x == self.x + 55 and i.y == self.y:
                        Cell.DrawCell(self)
                        cell_grid[self.y // 55][self.x // 55] = self.value
                        Cell.arrow_move(i)
    #nooltega liikumine
    def arrow_move(self):
        if not self.protected:
            tahvel.delete(self.number)
            self.number = tahvel.create_text(self.x + 25, self.y + 25, text="...")
            tahvel.tag_bind(self.number, '<1>', self.clicked)
            raam.bind("<Key>", self.keypress)
        else:
            raam.bind("<Key>", self.keypress)

    # teeb koha "..."'iks, ootab sisendit kasutajalt
    def clicked(self, event=None):
        if not self.protected:
            tahvel.delete(self.number)
            self.number = tahvel.create_text(self.x + 25, self.y + 25, text="...")
            tahvel.tag_bind(self.number, '<1>', self.clicked)
            raam.bind("<Key>", self.keypress)

    # tagastab asukoha ruudustikus
    def GetLocation(self):
        return self.x // 55, self.y // 55

# veerg - kontrollitav veerg
# int_cells - kõik listid argumendina
# märgid - leitud märgid reast
# duplikaate - kui True, leiti mitu ühesugust numbrit


def KontrolliVertikaalrida(int_cells, veerg, nulliga=False, tagasta_arv=False):
    märgid = []
    duplikaate = 0
    kontroll_list = []
    for i in range(9):
        kontroll_list.append(int_cells[i][veerg])
    for i in range(9):
        if nulliga:
            if not str(kontroll_list[i]) in märgid:
                märgid.append(str(kontroll_list[i]))
            else:
                duplikaate += 1
        else:
            if not str(kontroll_list[i]) == "0":
                if not str(kontroll_list[i]) in märgid:
                    märgid.append(str(kontroll_list[i]))
                else:
                    duplikaate += 1

    if not tagasta_arv:
        if duplikaate > 0:
            return True
        else:
            return False
    else:
        return duplikaate


raam = Tk()
raam.title("Sudoku")
raam.geometry("750x500")

tahvel = Canvas(raam, width=500, height=500, background="white")
tahvel.grid()

cell_grid = []
for i in range(9):
    one_grid = []
    for i in range(9):
        arv = 0
        one_grid.append(str(arv))
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
    # mida suurem on muutaja raskusaste, seda rohkem on vihjeid ette antud
    global cell_grid
    if not kasuta_näidist:
        raskusaste = 25
        if raskusaste_v2li.get().isnumeric():
            raskusaste = int(raskusaste_v2li.get())
            if raskusaste < 15 or raskusaste > 45:
                messagebox.showerror("Raskusaste pole sobiv", "Sisestage arv vahemikus 15-45.")
                return
        else:
            messagebox.showerror("Raskusaste pole sobiv", "Palun sisestage arv")
            return
        ute = 0
        while raskusaste >= ute:
            cell_grid = []
            for i in range(9):
                one_grid = []
                for j in range(9):
                    arv = 0
                    one_grid.append(arv)
                cell_grid.append(one_grid)
            ute = 0
            """
            # genereeri numbrid
            for column in range(3):
                trial = 90001
                while trial > 1000:
                    jupid1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for z in range(0, 7, 3):
                        row = z - 1
                        for i in range(3):
                            offset = randint(z, z + 2) - z + (column * 3)
                            if randint(0, 1):
                                row += 1
                            if row > len(cell_grid) - 1:
                                row = len(cell_grid) - 1
                            if row == z - 1:
                                row = z
                            trial = 0

                            r1 = randint(0, len(jupid1) - 1)
                            if len(cell_grid[row]) >= offset + 1:
                                while int(cell_grid[row][offset]) > 0:
                                    row = randint(z, z + 2)
                                    offset = randint(z, z + 2) - z + (column * 3)
                                cell_grid[row][offset] = jupid1[r1]
                            else:
                                cell_grid[row][offset] = 0
                            while KontrolliHorisontaalrida(cell_grid, row) or KontrolliVertikaalrida(cell_grid, offset):
                                if not KontrolliSisemist(cell_grid, column + 1 + z):
                                    cell_grid[row][offset] = 0
                                    row = randint(z, z + 2)
                                    offset = randint(z, z + 2) - z + (column * 3)
                                    r1 = randint(0, len(jupid1) - 1)
                                    cell_grid[row][offset] = jupid1[r1]
                            jupid1.remove(jupid1[r1])"""

            # lisab rohkem numbreid väljakule, et muuta mäng võimalikuks
            for i in range(9):
                x_off = 0
                y_off = 0
                if i == 1:
                    x_off = 3
                    y_off = 0
                elif i == 2:
                    x_off = 6
                    y_off = 0
                elif i == 3:
                    x_off = 0
                    y_off = 3
                elif i == 4:
                    x_off = 3
                    y_off = 3
                elif i == 5:
                    x_off = 6
                    y_off = 3
                elif i == 6:
                    x_off = 0
                    y_off = 6
                elif i == 7:
                    x_off = 3
                    y_off = 6
                elif i == 8:
                    x_off = 6
                    y_off = 6
                jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for y in range(y_off, y_off + 3):
                    for x in range(x_off, x_off + 3):
                        if cell_grid[y][x] in jupid:
                            jupid.remove(cell_grid[y][x])
                bad = True
                cycles = 0
                while bad:
                    if cycles > 9000:
                        break
                    jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for y in range(y_off, y_off + 3):
                        for x in range(x_off, x_off + 3):
                            if cell_grid[y][x] in jupid:
                                jupid.remove(cell_grid[y][x])
                    for y in range(y_off, y_off + 3):
                        for x in range(x_off, x_off + 3):
                            if int(cell_grid[y][x]) == 0:
                                r1 = randint(0, len(jupid) - 1)
                                cell_grid[y][x] = jupid[r1]
                                bad = False
                                while KontrolliHorisontaalrida(cell_grid, y) or KontrolliVertikaalrida(cell_grid, x) or KontrolliSisemist(cell_grid, i + 1):
                                    r1 = randint(0, len(jupid) - 1)
                                    cell_grid[y][x] = jupid[r1]
                                    jupid.remove(jupid[r1])
                                    if len(jupid) == 0:
                                        bad = True
                                        cell_grid[y][x] = 0
                                        break
                                    if not (KontrolliHorisontaalrida(cell_grid, y) or KontrolliVertikaalrida(cell_grid, x) or KontrolliSisemist(cell_grid, i + 1)):
                                        bad = False
                                        break
                            if bad:
                                break
                        if bad:
                            cycles += 1
                            break

            """cycles = 0
                                            bad = False
                                            for i in range(0, 8):
                                                if KontrolliHorisontaalrida(cell_grid, y) or KontrolliVertikaalrida(cell_grid, x) or KontrolliSisemist(cell_grid, i + 1):
                                                    for i in range(3):
                                                        cell_grid[y_off + i][x_off] = 0
                                                        cell_grid[y_off + i][x_off + 1] = 0
                                                        cell_grid[y_off + i][x_off + 2] = 0
                                                        jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                                        for u in range(y_off, y_off + 3):
                                                            for v in range(x_off, x_off + 3):
                                                                if cell_grid[u][v] in jupid:
                                                                    jupid.remove(cell_grid[u][v])
                                                        r1 = randint(0, len(jupid) - 1)
                                                        cell_grid[y][x] = jupid[r1]
                                                        bad = True
                                                        cycles += 1
                                                    #if cycles > 10:
                                                    #    print("tsükkel " + str(cycles))
                                                    #    for i in range(3):
                                                    #        cell_grid[y_off + i][x_off] = 0
                                                    #        cell_grid[y_off + i][x_off + 1] = 0
                                                    #        cell_grid[y_off + i][x_off + 2] = 0
                                                    #    break
                                                cycles += 1
            """
            # kontrollib võimalikke võimatuid olukordasid
            """for r in range(len(cell_grid)):
                testlen = len(cell_grid[r])
                for x in range(testlen):
                    cell_backup = cell_grid[r][x]
                    for i in range(9):
                        if cell_backup == 0:
                            nat = i + 1
                            cell_grid[r][x] = nat
                            dupes = DuplikaatideArv(cell_grid, x, r)
                            if dupes > 1:
                                for element in LeiaHorisontaalsedDuplikaadid(cell_grid, r):
                                    cell_grid[element[1]][element[0]] = 0
                                for element in LeiaVertikaalsedDuplikaadid(cell_grid, x):
                                    cell_grid[element[1]][element[0]] = 0
                        cell_grid[r][x] = cell_backup
            currentstate = True
            for i in range(1, 9, 1):
                if KontrolliSisemist(cell_grid, i, False):
                    currentstate = False
                if KontrolliVertikaalrida(cell_grid, i, False):
                    currentstate = False
            for i in range(0, 9, 1):
                if KontrolliHorisontaalrida(cell_grid, i, False):
                    currentstate = False
            if not currentstate:
                for i in range(len(cell_grid)):
                    cell_grid[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]"""
            global solved_grid
            solved_grid = []
            for element in cell_grid:
                solved_grid.append(element)
            for row in cell_grid:
                for i in row:
                    if not int(i) == 0:
                        ute += 1
            for i in range(ute - raskusaste):
                r1 = randint(0, 8)
                r2 = randint(0, 8)
                if int(cell_grid[r1][r2]) == 0:
                    while int(cell_grid[r1][r2]) == 0:
                        r1 = randint(0, 8)
                        r2 = randint(0, 8)
                    cell_grid[r1][r2] = 0
                else:
                    cell_grid[r1][r2] = 0
    else:
        cell_grid = []
        for i, a in enumerate(näidis):
            one_grid = []
            for j, b in enumerate(a):
                one_grid.append(näidis[i][j])
            cell_grid.append(one_grid)

    # see koodujupp eemaldab teatud numbrid kastidest
    # kuni kaks korda
    # hetkel pole kasutusel

    # kuvab numbrid ekraanile
    global cells
    cells = []
    for i in range(0, 9):
        for j in range(0, 9):
            outpt = str(cell_grid[i][j]).replace("0", "0")
            if cell_grid[i][j] == 0:
                prt = False
            else:
                prt = True
            cell = Cell(j * 55, i * 55, outpt, prt, cell_grid)
            cells.append(cell)

    DrawLines()

    for cell in cells:
        cell.DrawCell()


# Kontrollib lahendust, nüüd toimib
def CheckBtn():
    global cell_grid
    check_cells(cell_grid)


def SolveBtn():
    global solved_grid
    messagebox.showinfo("more things tbd", str(solved_grid).replace("],", "\n").replace("[", "").replace("]", ""))


def check_cells(c_g):
    currentstate = True
    for i in range(1, 9, 1):
        if KontrolliSisemist(c_g, i, True):
            currentstate = False
        if KontrolliVertikaalrida(c_g, i, True):
            currentstate = False
        if KontrolliHorisontaalrida(c_g, i, True):
            currentstate = False
    if currentstate:
        messagebox.showinfo("Lahenduse kontroll", "Lahendus õige!")
    else:
        messagebox.showerror("Lahenduse kontroll", "Lahendus vale!")


# kontrollib horistonaalset rida


def KontrolliHorisontaalrida(int_cells, rida, nulliga=False, tagasta_arv=False):
    märgid = []
    duplikaate = 0
    kontroll_check = int_cells[rida]
    for i in range(9):
        if nulliga:
            if not str(kontroll_check[i]) in märgid:
                märgid.append(str(kontroll_check[i]))
            else:
                duplikaate += 1
        else:
            if not str(kontroll_check[i]) == "0":
                if not str(kontroll_check[i]) in märgid:
                    märgid.append(str(kontroll_check[i]))
                else:
                    duplikaate += 1
    if not tagasta_arv:
        if duplikaate > 0:
            return True
        else:
            return False
    else:
        return duplikaate




def LeiaHorisontaalsedDuplikaadid(int_cells, rida):
    märgid = []
    duplikaate = []
    kontroll_check = int_cells[rida]
    for i in range(9):
        if not str(kontroll_check[i]) == "0":
            if not str(kontroll_check[i]) in märgid:
                märgid.append(str(kontroll_check[i]))
            else:
                duplikaate.append([rida, i])
    return duplikaate


def LeiaVertikaalsedDuplikaadid(int_cells, veerg):
    märgid = []
    duplikaate = []
    kontroll_check = []
    for b in int_cells:
        kontroll_check.append(b[veerg])
    for i in range(9):
        if not str(kontroll_check[i]) == "0":
            if not str(kontroll_check[i]) in märgid:
                märgid.append(str(kontroll_check[i]))
            else:
                duplikaate.append([i, veerg])
    return duplikaate

def DuplikaatideArv(int_cells, y, x):
    märgid = []
    duplikaate = 0
    kontroll_check = []
    for b in int_cells:
        kontroll_check.append(b[x])
    for i in range(9):
        if not str(kontroll_check[i]) == "0":
            if not str(kontroll_check[i]) in märgid:
                märgid.append(str(kontroll_check[i]))
            else:
                duplikaate += 1
    kontroll_check = int_cells[y]
    for i in range(9):
        if not str(kontroll_check[i]) == "0":
            if not str(kontroll_check[i]) in märgid:
                märgid.append(str(kontroll_check[i]))
            else:
                duplikaate += 1
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


def KontrolliSisemist(int_cells, kast, nulliga=False):
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
                if not int(int_cells[offset_y + i][offset_x + j]) in märgid:
                    märgid.append(int(int_cells[offset_y + i][offset_x + j]))
                else:
                    duplikaate = True
            else:
                if not int(int_cells[offset_y + i][offset_x + j]) == 0:
                    if not int(int_cells[offset_y + i][offset_x + j]) in märgid:
                        märgid.append(int(int_cells[offset_y + i][offset_x + j]))
                    else:
                        duplikaate = True
    return duplikaate


def CheckAuto():
    global kasuta_näidist
    if kasuta_näidist:
        kasuta_näidist = False
    elif not kasuta_näidist:
        kasuta_näidist = True


# joonistab ruudustiku
def Draw(cell_grid, cells):
    DrawLines()
    uus_mäng = Button(raam, text="Uus mäng", command=NewGame)
    uus_mäng.place(x=525, y=200)
    raskusaste_label = Label(raam, text="Vihjeid:")
    raskusaste_label.place(x=525, y=300)
    global raskusaste_v2li
    raskusaste_v2li = Entry(raam, width=2)
    raskusaste_v2li.insert(0, "25")
    raskusaste_v2li.place(x=600, y=300)
    for i in cells:
        Cell.DrawCell(i)
    kontrolli = Button(raam, text="Kontrolli", command=CheckBtn)
    kontrolli.place(x=525, y=250)
    lahendus = Button(raam, text="Lahendus (hetkel ei toimi)", command=SolveBtn)
    lahendus.place(x=525, y=150)
    var = 0
    global autocheck
    autocheck = Checkbutton(raam, text="Kasuta näidist", variable=var, command=CheckAuto)
    autocheck.place(x=525, y=370)
    NewGame()


while True:
    cells = []
    # loob Cell() objektid
    for i in range(0, 9):
        for j in range(0, 9):
            outpt = str(cell_grid[i][j]).replace("0", "0")
            cell = Cell(j * 55, i * 55, outpt, False, cell_grid)
            cells.append(cell)
    Draw(cell_grid, cells)
    raam.mainloop()
