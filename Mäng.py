from tkinter import *
from tkinter import messagebox
from random import *

# Sudoku projekt
# versioon 1.0

# näidis on etteantud lahendatav sudoku
näidis = []
# tase määrab mängu raskusastme
tase = 1


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
        textcol = "black"
        # else:
        #    textcol = "black"
        if KontrolliVertikaalrida(self.cell_grid, self.x // 55) or KontrolliHorisontaalrida(self.cell_grid,
                                                                                            self.y // 55) or KontrolliSisemist(
                self.cell_grid, LeiaSuurKast(self.x // 55, self.y // 55)):
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
                self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), font='Arial 12 bold',
                                                 fill="white")
            else:
                self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value), font='Arial 12 bold',
                                                 fill="black")
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
                    # print("Vertikaalne: " + str(KontrolliVertikaalrida(self.cell_grid, self.x // 55)))
                    # print("Horisontaalne: " + str(KontrolliHorisontaalrida(self.cell_grid, self.y // 55)))
                    # print("Sisemine: " + str(KontrolliSisemist(self.cell_grid, LeiaSuurKast(self.x // 55, self.y // 55))))
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

    # nooltega liikumine
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

# Kontrollib vertikaalset rida
def KontrolliVertikaalrida(int_cells, veerg, nulliga=False):
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
    if duplikaate > 0:
        return True
    else:
        return False


# tkinteri raami loomine
raam = Tk()
raam.title("Sudoku 1.0")
raam.geometry("750x500")

# tahvli lisamine
tahvel = Canvas(raam, width=500, height=500, background="white")
tahvel.grid()

# loo sudoku ruudustik 2D massiivina, kus
# üks list on üks rida
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

# uue mängu funktsioon
# see käivitatakse mängu laadimisel ja nupu "Uus mäng" vajutamisel


def NewGame():
    possible_easy = []
    possible_medium = []
    possible_hard = []
    global cell_grid
    current = cell_grid
    while cell_grid == current:
        for l in open("Sudokud.rdt", "r"):
            if not l.strip()[0] == "#" and l.strip()[0] == "[":
                fullrow = l.strip().replace("[", "").replace("]", "")
                level = fullrow.split(":")[0]
                content = fullrow.split(":")[1].replace(".", "000").replace(",", "00")
                if level == "l=1":
                    levellist = []
                    for j in range(9):
                        helplist = []
                        for i in range(j * 9, j * 9 + 9):
                            helplist.append(int(content[i]))
                        levellist.append(helplist)
                    possible_easy.append(levellist)
                elif level == "l=2":
                    levellist = []
                    for j in range(9):
                        helplist = []
                        for i in range(j * 9, j * 9 + 9):
                            helplist.append(int(content[i]))
                        levellist.append(helplist)
                    possible_medium.append(levellist)
                elif level == "l=3":
                    levellist = []
                    for j in range(9):
                        helplist = []
                        for i in range(j * 9, j * 9 + 9):
                            helplist.append(int(content[i]))
                        levellist.append(helplist)
                    possible_hard.append(levellist)
        cell_grid = []
        if tase == 1:
            näidis = possible_easy[randint(0, len(possible_easy) - 1)]
        elif tase == 2:
            näidis = possible_medium[randint(0, len(possible_medium) - 1)]
        else:
            näidis = possible_hard[randint(0, len(possible_hard) - 1)]
        for i, a in enumerate(näidis):
            one_grid = []
            for j, b in enumerate(a):
                one_grid.append(näidis[i][j])
            cell_grid.append(one_grid)

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


# Kontrollib, kas kõik on õige ühes 3x3 ruudustikus
def KontrolliKõikSisemised(int_cells):
    ret = False
    for i in range(9):
        if not KontrolliSisemist(int_cells, i + 1) == ret:
            ret = True
    return ret

# Lahendaja kood
# sain tööle :D
def SolveBtn():
    # määra cell_grid globaalseks muutujaks (muudatused toimuvad ka väljaspool tkinteri sündmust)
    global cell_grid
    # tsüklid - proovib 200 korda leida lahendust sudokule
    cycles = 0
    # peamine while tsükkel
    while True:
        # solveone lahendab kõik lihtsasti leitavad üksused
        prempties = 0
        for row in cell_grid:
            for item in row:
                if str(item) == "0":
                    prempties += 1
        SolveOne()
        cycles += 1
        # kontrollitakse, kas on alles tühjasid ruute
        # kui pole, siis tsükkel peatatakse
        empties = 0
        for row in cell_grid:
            for item in row:
                if str(item) == "0":
                    empties += 1
        if empties == 0:
            break

        # keerulisemate sudokude võib olla vajalik ka üksikute 3x3 sektsioonide
        # eraldi kontrollimine
        trybox = 0
        if empties == prempties:
            bigboxes = []
            for kast in range(1, 10, 1):
                if kast <= 3:
                    offx = (kast - 1) * 3
                    offy = 0
                elif 3 < kast < 6:
                    offx = (kast - 4) * 3
                    offy = 3
                elif kast > 6:
                    offx = (kast - 7) * 3
                    offy = 6
                empties = 0
                for i in range(offy, offy + 2, 1):
                    for j in range(offx, offx + 2, 1):
                        if int(cell_grid[i][j]) == 0:
                            empties += 1
                bigboxes.append(empties)
            smallest = 999
            for j, bb in enumerate(bigboxes):
                if 0 < bb < smallest:
                    smallest = bb
                    trybox = j + 1
        if trybox > 0:
            # viimane abinõu: kontrolli üksikuid ruute suures kastis
            for kast in range(trybox, trybox + 1, 2):
                if kast <= 3:
                    offx = (kast - 1) * 3
                    offy = 0
                elif 3 < kast < 6:
                    offx = (kast - 4) * 3
                    offy = 3
                elif kast > 6:
                    offx = (kast - 7) * 3
                    offy = 6
                empties = 0
                empty_cells = []
                candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(offy, offy + 2, 1):
                    for j in range(offx, offx + 2, 1):
                        if not str(cell_grid[i][j]) == "0":
                            if int(cell_grid[i][j]) in candidates:
                                candidates.remove(int(cell_grid[i][j]))
                        else:
                            empty_cells.append([j, i])
                if empties < 4:
                    for candidate in candidates:
                        for one in empty_cells:
                            if str(cell_grid[one[1]][one[0]]) == "0":
                                cell_backup = cell_grid[one[1]][one[0]]
                                cell_grid[one[1]][one[0]] = candidate
                                if KontrolliHorisontaalrida(cell_grid, one[1]) or KontrolliVertikaalrida(cell_grid, one[0]) or\
                                    KontrolliSisemist(cell_grid, LeiaSuurKast(one[0] + 1, one[1] + 1)):
                                    cell_grid[one[1]][one[0]] = cell_backup
        # teade kasutajale, juhul kui sudokut ei saa mingil põhjusel lahendada
        if cycles > 350:
            messagebox.showerror("Lahenduse leidmine nurjus", "Lahendust ei leitud. Võite proovida järgnevat:\n - Kustutage ruudud valede arvudega\n"
                                " - Proovige teist Sudokut")
            break
    # kuvab muudatused ekraanile
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


# Kontrollib lahendust
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



# Lahendaja (jätk)
def SolveOne():
    global cell_grid
    solutions = []
    prev_grid = cell_grid
    # kontrolli ridu
    for y in range(9):
        row = cell_grid[y]
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for item in row:
            if int(item) in candidates:
                candidates.remove(int(item))
        empties = 9 - len(candidates)
        if empties == 8:
            for x in range(len(row)):
                if int(cell_grid[y][x]) == 0:
                    cell_grid[y][x] = candidates[-1]

    # kontrolli veerge
    for x in range(9):
        veerg = []
        for y in range(9):
            veerg.append(cell_grid[y][x])
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for item in veerg:
            if str(item) in str(candidates):
                candidates.remove(int(item))
        empties = 9 - len(candidates)
        if empties == 8:
            for y in range(len(veerg)):
                if int(cell_grid[y][x]) == 0:
                    cell_grid[y][x] = candidates[-1]
    # kontrolli üksikuid ruute
    for i in range(9):
        for y in range(9):
            for x in range(9):
                box = LeiaSuurKast(x, y)
                offx = 0
                offy = 0
                if box < 4:
                    offy = 0
                    offx = (box - 1) * 3
                elif 3 < box < 6:
                    offy = 3
                    offx = (box - 4) * 3
                elif box >= 6:
                    offy = 6
                    offx = (box - 7) * 3
                # kuumkohad
                spots = [0, 0, 0,
                         0, 0, 0,
                         0, 0, 0]
                # kontrollitavad ruudud
                checkables = [[offy, offx], [offy, offx + 1], [offy, offx + 2],
                              [offy + 1, offx], [offy + 1, offx + 1], [offy + 1, offx + 2],
                              [offy + 2, offx], [offy + 2, offx + 1], [offy + 2, offx + 2]]
                checked_grid = []
                position_grid = []
                total_hots = 0
                for l, thing in enumerate(checkables):
                    checked_grid.append(cell_grid[thing[0]][thing[1]])
                    position_grid.append((thing[0], thing[1]))
                    cell_backup = cell_grid[thing[0]][thing[1]]
                    if str(cell_grid[thing[0]][thing[1]]) == str(i + 1):
                        break
                    if str(cell_grid[thing[0]][thing[1]]) == "0":
                        cell_grid[thing[0]][thing[1]] = str(i + 1)
                        if not KontrolliSisemist(cell_grid, l + 1):
                            if KontrolliHorisontaalrida(cell_grid, thing[0]):
                                spots[l] += 1
                                total_hots += 1
                            elif KontrolliVertikaalrida(cell_grid, thing[1]):
                                spots[l] += 1
                                total_hots += 1
                        else:
                            total_hots = 9
                            spots[l] += 1
                            cell_grid[thing[0]][thing[1]] = cell_backup
                            break
                        cell_grid[thing[0]][thing[1]] = cell_backup
                    else:
                        spots[l] += 1
                        total_hots += 1
                if total_hots == 8:
                    for p in range(9):
                        if spots[p] == 0:
                            solutions.append((str(i + 1), position_grid[p]))
    if len(solutions) > 0:
        cell_grid[solutions[0][1][0]][solutions[0][1][1]] = solutions[0][0][0]
    # leia üksikuid võimalusi (nt ainus arv, mis rea esimesse tühja kohta sobib on 7, teise tühja kohta sobib ainult 6)
    # veergudest ja ridadest
    if cell_grid == prev_grid:
        for g in range(9):
            for arv in range(9):
                goodies = 0
                good = 0
                for subarv in range(9):
                    cell_backup = cell_grid[arv][subarv]
                    if int(cell_backup) == 0:
                        cell_grid[arv][subarv] = (g + 1)
                        if not(KontrolliVertikaalrida(cell_grid, subarv) or KontrolliHorisontaalrida(cell_grid, arv) or KontrolliSisemist(cell_grid, LeiaSuurKast(subarv, arv))):
                            goodies += 1
                            good = subarv
                        cell_grid[arv][subarv] = cell_backup
                if goodies == 1:
                    cell_grid[arv][good] = (g + 1)

    if cell_grid == prev_grid:
        for g in range(9):
            for column in range(9):
                goodies = 0
                good = 0
                for row in range(9):
                    cell_backup = cell_grid[row][column]
                    if int(cell_backup) == 0:
                        cell_grid[row][column] = (g + 1)
                        if not (KontrolliHorisontaalrida(cell_grid, row) or KontrolliVertikaalrida(cell_grid, column) or KontrolliSisemist(cell_grid, LeiaSuurKast(column, row))):
                            goodies += 1
                            good = row
                        cell_grid[row][column] = cell_backup
                if goodies == 1:
                    cell_grid[good][column] = (g + 1)

# kontrollib horistonaalset rida


def KontrolliHorisontaalrida(int_cells, rida, nulliga=False):
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
    if duplikaate > 0:
        return True
    else:
        return False


# raskusastme muutmine
def ChangeDiff():
    global tase
    global raskusaste_nupp
    tase += 1
    if tase > 3:
        tase = 1
    raskusaste_nupp.config(
        text="Raskusaste: " + str(tase).replace("1", "Kerge").replace("2", "Keskmine").replace("3", "Raske"))


# leiab suure kasti (3x3 ala) vastavalt väikse kasti (1 ruut) koordinaatidele

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


# Kontrollib, kas 3x3 sektsioon on õigesti lahendatud
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
def Draw(cell_grid, cells):
    DrawLines()
    uus_mäng = Button(raam, text="Uus mäng", command=NewGame)
    uus_mäng.place(x=525, y=200)

    global raskusaste_nupp
    raskusaste_nupp = Button(raam, text="Raskusaste: Kerge", command=ChangeDiff)
    raskusaste_nupp.place(x=525, y=300)
    for i in cells:
        Cell.DrawCell(i)
    kontrolli = Button(raam, text="Kontrolli", command=CheckBtn)
    kontrolli.place(x=525, y=250)
    lahendus = Button(raam, text="Lahenda", command=SolveBtn)
    lahendus.place(x=525, y=150)
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
