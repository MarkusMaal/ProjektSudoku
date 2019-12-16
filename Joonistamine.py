from tkinter import *
from tkinter import font
import time

raam = Tk()
raam.title("Sudoku")
raam.geometry("700x500")

tahvel = Canvas(raam, width=500, height=500, background="white")
tahvel.grid()

#joonistab paksemad jooned
def DrawLines():
    tahvel.create_rectangle(0, 0, 500, 500, fill="black")
    tahvel.create_line(0, 163, 500, 163, width=3, fill="white")
    tahvel.create_line(0, 328, 500, 328, width=3, fill="white")
    tahvel.create_line(163, 0, 163, 500, width=3, fill="white")
    tahvel.create_line(328, 0, 328, 500, width=3, fill="white")

#klass, milles üks objekt on 1 ruut
class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    #joonistab ruudu ja sisse numbri
    def DrawCell(self):
        self.joonis = tahvel.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill="white", outline="black", width=1, activefill="lightblue")
        self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value))
        tahvel.tag_bind(self.joonis, '<1>', self.clicked)
        tahvel.tag_bind(self.number, '<1>', self.clicked)

    #määrab numbri, mis cell'i/ruudu eelnevale numbrile asemele panna
    def keypress(self, event=None):
        if int(event.char) > 0 and int(event.char) < 10:
            self.value = event.char
            tahvel.delete(self.number)
            tahvel.delete(self.joonis)
            Cell.DrawCell(self)

    #teeb koha "..."'iks, ootab sisendit kasutajalt
    def clicked(self, event=None):
        print("clicked on", self.value)
        tahvel.delete(self.number)
        self.number = tahvel.create_text(self.x + 25, self.y + 25, text="...")
        tahvel.tag_bind(self.number, '<1>', self.clicked)
        raam.bind("<Key>", self.keypress)

cells = []

#loob Cell() objektid
for i in range(0, 9):
    for j in range(0, 9):
        cell = Cell(j*55, i*55, " ")
        cells.append(cell)

#joonistab ruudustiku
def Draw():
    DrawLines()
    for i in cells:
        Cell.DrawCell(i)
    uus_mäng = Button(raam, text="Uus mäng")
    uus_mäng.grid(row=0, column=1)
    kontrolli = Button(raam, text="Kontrolli")
    kontrolli.grid(row=0, column=2)

Draw()

raam.mainloop()