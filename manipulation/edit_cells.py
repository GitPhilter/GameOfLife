

def write_cells_to_cells(canvas_cells, paint_cells, x_offset, y_offset):
    x_counter = 0
    y_counter = 0
    for row in paint_cells:
        for cell in row:
            if y_counter + y_offset < len(canvas_cells) and x_counter + x_offset < len(canvas_cells[y_counter + y_offset]):
                canvas_cells[y_counter + y_offset][x_counter + x_offset] = paint_cells[y_counter][x_counter]
            x_counter += 1
        x_counter = 0
        y_counter += 1
    return canvas_cells


