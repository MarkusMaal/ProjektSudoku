print("Sudoku lisamine (arendustööriist)\n\n")
print(" * Raskusaste * ")
print("1. Kerge")
print("2. Keskmine")
print("3. Raske")
diff = 0
while diff < 1 or diff > 3:
    diff = int(input("Valige number: "))
print("\n\n\nSisestage arvud ühe rea kaupa (1 rida peab sisaldama 9-t arvu)")
rows = ""
for i in range(9):
    rcheck = ""
    while not len(rcheck) == 9:
        rcheck = input("Rida " + str(i + 1) + ": ")
    rows += rcheck
rows = rows.replace("000", ".").replace("00", ",")
fail = open("Sudokud.rdt", "a")
fail.write("\n[l=" + str(diff) + ":" + rows + "]")
fail.close()
