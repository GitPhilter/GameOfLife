import configurations.general


def get_pattern_1():
    strings = [
        ["D", "D", "D", "D", "D", "D", "A", "A", "D", "D"],
        ["D", "D", "D", "D", "D", "A", "D", "A", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "A", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "A", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "A", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "A", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    ]
    return configurations.general.get_cells_from_strings_2(strings, 100, 100, 45, 45)
