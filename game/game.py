import pygame


# parameters
import game.rules

cell_width = 8
cell_height = 8
cell_alive_color = (0, 255, 0)


def run_game_of_life(cells, win, delay):
    # x * y grid
    x = 200
    y = 100
    draw_cells(cells, win)
    print_cells(cells)
    pygame.time.delay(1000)
    #print("initial cells length:", len(cells))
    while True:
        #print("running...")
        # chill
        pygame.time.delay(delay)
        # do stuff
        pygame.event.pump()
        cells = game.rules.apply_rules(cells)
        # draw cells
        draw_cells(cells, win)


def run_game_of_life_no_graphics_one_step(cells):
    cells = game.rules.apply_rules(cells)

    return cells




def draw_cells(cells, win):
    win.fill((0, 0, 0))
    x_counter = 0
    y_counter = 0
    for row in cells:
        for cell in row:
            x = x_counter * cell_width
            y = y_counter * cell_height
            if cell == "A":
                pygame.draw.rect(win, cell_alive_color, (x + 1, y + 1, cell_width - 2, cell_height - 2))
            elif cell == "D":
                pygame.draw.rect(win, (0, 0, 0), (x + 1, y + 1, cell_width - 2, cell_height - 2))
            else:
                pygame.draw.rect(win, (0, 0, 255), (x + 1, y + 1, cell_width - 2, cell_height - 2))
            x_counter += 1
        x_counter = 0
        y_counter += 1
    pygame.display.update()


def print_cells(cells):
    for row in cells:
        for cell in row:
            if cell == "A":
                print("A", end=" ")
            elif cell == "D":
                print("D", end=" ")
            else:
                print("?", end=" ")
        print()
    print()

