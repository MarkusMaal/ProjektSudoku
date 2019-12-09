from tkinter import *
from tkinter import font
import time

raam = Tk()
raam.title("Sudoku")
raam.geometry("1080x480")

tahvel = Canvas(raam, width=900, height=900, background="white")
tahvel.grid()


#joonistab paksemad jooned
def DrawLines():
    tahvel.create_line(0, 163, 500, 163, width=3, fill="black")
    tahvel.create_line(0, 328, 500, 328, width=3, fill="black")
    tahvel.create_line(163, 0, 163, 500, width=3, fill="black")
    tahvel.create_line(328, 0, 328, 500, width=3, fill="black")

#klass, milles üks objekt on 1 ruut
class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def DrawCell(self):
        self.number = tahvel.create_text(self.x + 25, self.y + 25, text=str(self.value))
        self.joonis = tahvel.create_rectangle(self.x, self.y, self.x+50, self.y+50, outline="black", width=1, activefill="lightblue")

cells = []
DrawLines()

for i in range(0, 9):
    for j in range(0, 9):
        cell = Cell(j*55, i*55, "")
        cells.append(cell)
        #cell.value = cells.index(cell)

for i in cells:
    Cell.DrawCell(i)

raam.mainloop()