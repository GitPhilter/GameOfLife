

def get_cells_with_points(x_, y_, points, x_offset, y_offset):
    cells = []
    for y in range(0, y_):
        new_row = []
        for x in range(0, x_):
            new_row.append("D")
        cells.append(new_row)
    mark_cells_as_alive(cells, points, x_offset, y_offset)
    return cells


def get_empty_cells(x_, y_):
    cells = []
    for y in range(0, y_):
        new_row = []
        for x in range(0, x_):
            new_row.append("D")
        cells.append(new_row)
    return cells


def mark_cells_as_alive(cells, points, x_offset, y_offset):
    for p in points:
        cells[p[0] + y_offset][p[1] + x_offset] = "A"


def get_cells_from_strings(strings):
    cells = []
    for row in strings:
        new_row = []
        for c in row:
            new_row.append(c)
        cells.append(new_row)
    return cells


def get_cells_from_strings_2(strings, x_, y_, x_offset, y_offset):
    # empty grid
    cells = []
    for y in range(0, y_):
        new_row = []
        for x in range(0, x_):
            new_row.append("D")
        cells.append(new_row)

    for r in range(0, len(strings)):
        for c in range(0, len(strings[r])):
            cells[r + y_offset][c + x_offset] = strings[r][c]
    return cells

