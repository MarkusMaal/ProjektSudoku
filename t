
    row = 2
    for i in range(3):
        offset = randint(0, 2)
        r1 = randint(0, len(jupid1) - 1)
        row += 1
        cell_grid[row][offset] = jupid1[r1]
        jupid1.remove(jupid1[r1])

"""
    offset = 2
    jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    jupid_kh = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    fine = False
    while not fine:
        # üleval keskmine
        row = -1
        offset = 5
        jupid_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(3):
            xp = jupid_2[randint(0, len(jupid_2) - 1)]
            jupid_2.remove(xp)
            if xp == 6 or xp == 7 or xp == 8:
                row = 2
            elif xp == 3 or xp == 4 or xp == 5:
                row = 1
            else:
                row = 0
            r1 = randint(0, len(jupid) - 1)
            cell_grid[row][offset - row] = jupid[r1]
            cycles = 0
            fine = True
            while KontrolliHorisontaalrida(cell_grid, row):
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                # print(offset - row)
                cell_grid[row][offset - row] = jupid[r1]
                cycles += 1
                if cycles == 10:
                    fine = False
                    cell_grid[row][offset - row] = 0
                    break
            jupid.remove(jupid[r1])


    # keskmine
    fine = False
    while not fine:
        row = 3
        offset = 3
        jupid_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(3):
            xp = jupid_2[randint(0, len(jupid_2) - 1)]
            jupid_2.remove(xp)
            if xp == 6 or xp == 7 or xp == 8:
                row = 5
            elif xp == 3 or xp == 4 or xp == 5:
                row = 4
            else:
                row = 3
            r1 = randint(0, len(jupid) - 1)
            jupid_kh[row - 3].remove(jupid[r1])
            cell_grid[row][offset + xp - (row * 3)] = jupid[r1]
            cycles = 0
            fine = True
            while KontrolliVertikaalrida(cell_grid, offset + xp - (row * 3)):
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                cell_grid[row][offset + xp - (row * 3)] = jupid[r1]
                cycles += 1
                if cycles == 10:
                    fine = False
                    break
            jupid.remove(jupid[r1])

    # keskmine all
    fine = False
    while not fine:
        offset = 21
        jupid_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(3):
            xp = jupid_2[randint(0, len(jupid_2) - 1)]
            jupid_2.remove(xp)
            if xp == 6 or xp == 7 or xp == 8:
                row = 8
            elif xp == 3 or xp == 4 or xp == 5:
                row = 7
            else:
                row = 6
            if len(jupid) > 1:
                r1 = randint(0, len(jupid) - 1)
            else:
                r1 = 0
            cell_grid[row][offset + xp - (row * 3)] = jupid[r1]
            cycles = 0
            fine = True
            while KontrolliVertikaalrida(cell_grid, offset + xp - (row * 3)):
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                cell_grid[row][offset + xp - (row * 3)] = jupid[r1]
                cycles += 1
                if cycles == 10:
                    fine = False
                    break
            jupid.remove(jupid[r1])
    # ülemine parem

    jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = 0
    offset = 8
    for i in range(3):
        if i % 3 == 0:
            row += 1
        column = offset - (randint(0, 2))
        r1 = randint(0, len(jupid) - 1)
        cell_grid[row][column] = r1
        if not (KontrolliHorisontaalrida(cell_grid, row) or KontrolliVertikaalrida(cell_grid, column)):
            jupid.remove(jupid[r1])
        else:
            while KontrolliHorisontaalrida(cell_grid, row) or KontrolliVertikaalrida(cell_grid, column):
                r1 = randint(0, len(jupid) - 1)
                cell_grid[row][column] = r1
            jupid.remove(jupid[r1])
    fine = False
    jupid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cycles = 0
    while not fine:
        # keskpar
        offset = 11
        jupid_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(3):
            xp = jupid_2[randint(0, len(jupid_2) - 1)]
            jupid_2.remove(xp)
            if xp == 6 or xp == 7 or xp == 8:
                row = 5
            elif xp == 3 or xp == 4 or xp == 5:
                row = 4
            else:
                row = 3
            r1 = randint(0, len(jupid) - 1)
            cell_grid[row][offset - row] = jupid[r1]
            # print(cell_grid[row][offset - row - (row % 3)])
            cycles = 0
            fine = True
            while KontrolliHorisontaalrida(cell_grid, row) and KontrolliVertikaalrida(cell_grid, offset - row - (row % 3)):
                r1 += 1
                if r1 > len(jupid) - 1:
                    r1 = 0
                cell_grid[row][offset - row - (row % 3)] = jupid[r1]
                cycles += 1
                if cycles == 10:
                    fine = False
                    cell_grid[row][offset - row - (row % 3)] = 0
                    break
            jupid.remove(jupid[r1])
    """