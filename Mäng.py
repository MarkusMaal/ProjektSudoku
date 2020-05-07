from tkinter import *
from tkinter import font
from tkinter import messagebox
from random import *
import time


# Sudoku projekt
# klass, milles üks objekt on 1 ruut

class Cell:
    def __init__(self, x, y, value, protected, cell_grid):
        self.x = x
        self.y = y
        self.value = value
        self.protected = protected
        self.cell_grid = cell_grid

    # joonistab ruudu ja sisse numbri
    def DrawCell(self):
        self.joonis = tahvel.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill="white", outline="black",
                                              width=1, activefill="lightblue")
        if not self.protected:
            self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value))
        else:
            self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), font='Arial 12 bold')
        tahvel.tag_bind(self.joonis, '<1>', self.clicked)
        tahvel.tag_bind(self.number, '<1>', self.clicked)

    # määrab numbri, mis cell'i/ruudu eelnevale numbrile asemele panna
    def keypress(self, event):
        if 0 <= int(event.char) < 10:
            if not int(event.char) == 0:
                self.value = event.char
            else:
                self.value = " "
            self.cell_grid[self.y // 55][self.x // 55] = event.char
            print("Vertikaalne: " + str(KontrolliVertikaalrida(self.cell_grid, self.x // 55)))
            print("Horisontaalne: " + str(KontrolliHorisontaalrida(self.cell_grid, self.y // 55)))
            print("Sisemine: " + str(KontrolliSisemist(self.cell_grid, LeiaSuurKast(self.x // 55, self.y // 55))))
            tahvel.delete(self.number)
            tahvel.delete(self.joonis)
            Cell.DrawCell(self)

    # teeb koha "..."'iks, ootab sisendit kasutajalt
    def clicked(self, event=None):
        if not self.protected:
            tahvel.delete(self.number)
            self.number = tahvel.create_text(self.x + 25, self.y + 25, text="...")
            tahvel.tag_bind(self.number, '<1>', self.clicked)
            raam.bind("<Key>", self.keypress)


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
raam.geometry("700x500")

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


# Loo väli näidise põhjal
kasuta_näidist = True
näidis = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def NewGame():
    # mida suurem on muutaja raskusaste, seda rohkem on vihjeid ette antud
    global cell_grid
    if not kasuta_näidist:
        raskusaste = 35
        ute = 0
        while ute < raskusaste:
            cell_grid = []
            for i in range(9):
                one_grid = []
                for j in range(9):
                    arv = 0
                    one_grid.append(arv)
                cell_grid.append(one_grid)
            ute = 0
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
                            while KontrolliSisemist(cell_grid, column + 1 + z):
                                cell_grid[row][offset] = jupid1[randint(0, len(jupid1) - 1)]
                            while KontrolliHorisontaalrida(cell_grid, row) or KontrolliVertikaalrida(cell_grid, offset):
                                cell_grid[row][offset] = 0
                                row = randint(z, z + 2)
                                offset = randint(z, z + 2) - z + (column * 3)
                                r1 = randint(0, len(jupid1) - 1)
                                cell_grid[row][offset] = jupid1[r1]
                            jupid1.remove(jupid1[r1])

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
                for y in range(y_off, y_off + 2):
                    for x in range(x_off, x_off + 2):
                        if cell_grid[y][x] == 0:
                            r1 = randint(0, len(jupid) - 1)
                            cell_grid[y][x] = jupid[r1]
                            cycles = 0
                            while KontrolliHorisontaalrida(cell_grid, y) or KontrolliVertikaalrida(cell_grid, x):
                                if cycles > 10000:
                                    cell_grid[y][x] = 0
                                    break
                                r1 = randint(0, len(jupid) - 1)
                                cell_grid[y][x] = jupid[r1]
                                cycles += 1

            # kontrollib võimalikke võimatuid olukordasid
            for r in range(len(cell_grid)):
                testlen = len(cell_grid[r])
                for x in range(testlen):
                    cell_backup = cell_grid[r][x]
                    for i in range(9):
                        nat = i + 1
                        cell_grid[r][x] = nat
                        dupes = KontrolliVertikaalrida(cell_grid, x, False, True) + KontrolliHorisontaalrida(cell_grid,
                                                                                                             r,
                                                                                                             False,
                                                                                                             True)
                        if dupes > 1:
                            cell_grid[r][x] = 0
                        else:
                            cell_grid[r][x] = cell_backup
            for row in cell_grid:
                for i in row:
                    if not int(i) == 0:
                        ute += 1
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
    """for i in range(3):
        for j in range(9):
            r1 = randint(0, 8)
            cell_grid[j][r1] = 0"""

    # kuvab numbrid ekraanile
    cells = []
    for i in range(0, 9):
        for j in range(0, 9):
            outpt = str(cell_grid[i][j]).replace("0", " ")
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


def check_cells(c_g):
    print(c_g)
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


# joonistab ruudustiku
def Draw(cell_grid):
    DrawLines()
    uus_mäng = Button(raam, text="Uus mäng", command=NewGame)
    uus_mäng.place(x=525, y=200)
    raskusaste_label = Label(raam, text="Raskusaste:")
    raskusaste_label.place(x=525, y=300)
    raskusaste = Entry(raam, width=2)
    raskusaste.place(x=600, y=300)
    for i in cells:
        Cell.DrawCell(i)
    kontrolli = Button(raam, text="Kontrolli", command=CheckBtn)
    kontrolli.place(x=525, y=250)
    var = 0
    abistajad = Checkbutton(raam, text="Abistajad", variable=var)
    abistajad.place(x=525, y=350)



while True:
    cells = []
    # loob Cell() objektid
    for i in range(0, 9):
        for j in range(0, 9):
            outpt = str(cell_grid[i][j]).replace("0", " ")
            cell = Cell(j * 55, i * 55, outpt, False, cell_grid)
            cells.append(cell)
    Draw(cell_grid)
    raam.mainloop()
