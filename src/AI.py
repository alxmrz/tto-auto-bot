def find_next_click(cells):
    print("CELLS: ", cells)

    for cells_row in cells:
        for cell in cells_row:
            print(cell)
            if cell[2] == 'N':
                return cell

    return None