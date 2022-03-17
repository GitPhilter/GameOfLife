import random
import configurations.random_configurations
import configurations.general
import manipulation.edit_cells
import game.game


def find_pattern():
    total_width = 20
    total_height = 20
    considered_box_width = 10
    considered_box_height = 10
    considered_box_x = round(total_width / 2 - considered_box_width / 2)
    considered_box_y = round(total_height / 2 - considered_box_height / 2)
    max_simulation_steps = 100000
    max_cycle_steps_considered = 20
    previous_states = []
    step_counter = 0
    percentage = random.randint(1, 99)
    random_cells = configurations.random_configurations.get_random_starting_configuration(10, 10, percentage)
    cells = configurations.general.get_empty_cells(total_width, total_height)
    print(cells)
    print("len(cells)", len(cells))
    print("len(cells[0]", len(cells[0]))
    cells = manipulation.edit_cells.write_cells_to_cells(cells, random_cells, considered_box_x, considered_box_y)
    while step_counter < max_simulation_steps:
        print("step no", step_counter)
        current_state = get_cells_subsquare(cells, 0, 0,
                                                   total_width, total_height)
        if all_cells_are_dead(current_state):
            print("Lol, alle tot, lolz")
            random_cells = configurations.random_configurations.get_random_starting_configuration(10, 10, percentage)
            cells = configurations.general.get_empty_cells(total_width, total_height)
            cells = manipulation.edit_cells.write_cells_to_cells(cells, random_cells, considered_box_x,
                                                                 considered_box_y)

        if current_state in previous_states:
            # detect length of cycle:
            index = previous_states.index(current_state)
            length_of_cycle = len(previous_states) - index
            #print("LENGTH OF CYCLE FOUND:", length_of_cycle)
            if length_of_cycle >= 4:
                # game.game.print_cells(current_state)
                return current_state
        else:
            previous_states.append(current_state)

        if len(previous_states) > max_cycle_steps_considered:
            del(previous_states[0])
        cells = game.game.run_game_of_life_no_graphics_one_step(cells)

        step_counter += 1
    return None

def all_cells_are_dead(cells):
    for row in cells:
        for cell in row:
            if cell == "A":
                return False
    return True

def get_cells_subsquare(cells, x_, y_, width, height):
    result_cells = []
    for y in range(y_, y_ + height):
        new_row = []
        for x in range(x_, x_ + width):
            #print("y:", y, ", x:", x)
            new_row.append(cells[y][x])
        result_cells.append(new_row)
    return result_cells
