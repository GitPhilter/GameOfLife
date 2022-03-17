

def apply_rules(cells):
    x_counter = 0
    y_counter = 0
    new_cells = []
    for row in cells:
        new_row = []
        for cell in row:
            alive_neighbours = get_number_of_alive_neighbours(cells, x_counter, y_counter)
            if cell == "D" and alive_neighbours == 3:
                new_row.append("A")
            elif cell == "A" and not 1 < alive_neighbours < 4:
                new_row.append("D")
            else:
                new_row.append(cell)
            x_counter += 1
        new_cells.append(new_row)
        x_counter = 0
        y_counter += 1
    return new_cells


def get_number_of_alive_neighbours(cells, x, y):
    result = 0
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if a != 0 or b != 0:
                current_x = b + x
                current_y = a + y
                if 0 <= current_x < len(cells[0]) and 0 <= current_y < len(cells):
                    if cells[current_y][current_x] == "A":
                        result += 1
    return result
