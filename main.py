import pygame
import os

import patterns.pattern_finder
import game.game

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
import configurations.random_configurations
import configurations.simple_configurations
import configurations.general
import configurations.cool_configurations
import configurations.patterns_found

cell_width = 5
cell_height = 5
cell_frame_color = (255, 0, 0)
cell_alive_color = (0, 255, 0)

def run_game_of_life():
    # x * y grid
    x = 200
    y = 100
    #cells = configurations.random_configurations.get_random_starting_configuration(x, y, 12)
    # cells = configurations.simple_configurations.get_test_4()
    #strings = [
        #["A", "A", "D"],
        #["A", "D", "A"],
        #["A", "D", "D"]
    #]
    #cells = configurations.general.get_cells_from_strings_2(strings, 100, 50, 50, 25)
    cells = configurations.cool_configurations.get_cool_thing_6()
    draw_cells(cells)
    print_cells(cells)
    pygame.time.delay(1000)
    #print("initial cells length:", len(cells))
    while True:
        #print("running...")
        # chill
        # pygame.time.delay(200)
        # do stuff
        pygame.event.pump()
        cells = apply_rules(cells)
        # draw cells
        draw_cells(cells)


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
    # if result != 0:
        # print("result:", result)
    return result


def apply_rules(cells):
    x_counter = 0
    y_counter = 0
    new_cells = []
    for row in cells:
        new_row = []
        for cell in row:
            alive_neighbours = get_number_of_alive_neighbours(cells, x_counter, y_counter)
            # alive_neighbours = 0
            if cell == "D" and alive_neighbours == 3:
                new_row.append("A")
            elif cell == "A" and not 1 < alive_neighbours < 4:
                new_row.append("D")
            else:
                new_row.append(cell)
            x_counter += 1
        #print("row length:", len(row))
        #print("new_row length:", len(new_row))
        new_cells.append(new_row)
        x_counter = 0
        y_counter += 1
    #print("new_cells length", len(new_cells))
    return new_cells


def draw_cells(cells):
    win.fill((0, 0, 0))
    x_counter = 0
    y_counter = 0
    #global cell_frame_color, cell_alive_color
    for row in cells:
        for cell in row:
            x = x_counter * cell_width
            y = y_counter * cell_height
            #pygame.draw.rect(win, cell_frame_color, (x, y, cell_width, cell_height))
            if cell == "A":
                pygame.draw.rect(win, cell_alive_color, (x + 1, y + 1, cell_width - 2, cell_height - 2))
            elif cell == "D":
                pygame.draw.rect(win, (0, 0, 0), (x + 1, y + 1, cell_width - 2, cell_height - 2))
            else:
                pygame.draw.rect(win, (0, 0, 255), (x + 1, y + 1, cell_width - 2, cell_height - 2))



            #print("drawing rect.")
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

if __name__ == "__main__":
    print("SpaceHunter.main()")
    width = 1200
    height = 800
    # init and error check
    (numpass, numfail) = pygame.init()
    print("number of modules booted successfully: ", numpass)
    print("number of modules not booted: ", numfail)
    # set window
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("+++ Game Of Life +++")
    # (x, y) = win.get_size()
    run_game_of_life()
    #pattern = patterns.pattern_finder.find_pattern()
    #if pattern is not None:
        #game.game.run_game_of_life(pattern, win, 200)
    # cells = configurations.patterns_found.get_pattern_1()
    # game.game.run_game_of_life(cells, win)


