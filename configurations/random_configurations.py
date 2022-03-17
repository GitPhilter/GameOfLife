from random import randint


def get_random_starting_configuration(width, height, percentage_alive):
    cells = []
    for y in range(0, height):
        new_row = []
        for x in range(0, width):
            rnd = randint(1, 100)
            if rnd > percentage_alive:
                new_row.append("D")
            else:
                new_row.append("A")
        cells.append(new_row)
    return cells


