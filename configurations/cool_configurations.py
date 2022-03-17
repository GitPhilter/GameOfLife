from configurations import general


def get_cool_thing_1():
    strings = [
        ["A", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["D", "A", "D", "D", "A", "D", "D", "A", "D"],
        ["D", "D", "A", "A", "A", "D", "A", "D", "D"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["A", "A", "D", "A", "D", "A", "D", "A", "A"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["D", "D", "A", "D", "A", "A", "A", "D", "D"],
        ["D", "A", "D", "D", "A", "D", "D", "A", "D"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "A"]
    ]
    return general.get_cells_from_strings_2(strings, 200, 100, 40, 20)


def get_cool_thing_2():
    strings = [
        ["D", "A", "A", "D", "D", "D", "A", "A", "D"],
        ["D", "A", "D", "A", "A", "A", "D", "A", "D"],
        ["A", "D", "A", "D", "A", "D", "A", "D", "A"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["D", "A", "A", "A", "A", "A", "A", "A", "D"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["A", "D", "A", "D", "A", "D", "A", "D", "A"],
        ["D", "A", "D", "A", "A", "A", "D", "A", "D"],
        ["D", "A", "A", "D", "D", "D", "A", "A", "D"]
    ]
    return general.get_cells_from_strings_2(strings, 160, 80, 60, 30)



def get_cool_thing_3():
    strings = [
        ["A", "D", "D", "D", "A", "D", "D", "D", "A"],
        ["A", "D", "D", "D", "A", "D", "D", "D", "A"],
        ["A", "A", "D", "A", "D", "A", "D", "A", "A"],
        ["D", "D", "A", "D", "A", "D", "A", "D", "D"],
        ["D", "A", "D", "A", "D", "A", "D", "A", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["A", "D", "A", "D", "A", "D", "A", "D", "A"],
        ["D", "A", "D", "A", "D", "A", "D", "A", "D"],
        ["A", "D", "A", "D", "A", "D", "A", "D", "A"]
    ]
    return general.get_cells_from_strings_2(strings, 320, 160, 160, 80)


def get_cool_thing_4():
    strings = [
        ["D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["D", "D", "D", "A", "D", "A", "D", "D", "D"],
        ["D", "D", "A", "D", "A", "D", "A", "D", "D"],
        ["D", "D", "D", "A", "A", "A", "D", "D", "D"],
        ["D", "D", "D", "D", "A", "D", "D", "D", "D"],
        ["D", "D", "D", "A", "D", "A", "D", "D", "D"],
        ["D", "D", "A", "A", "A", "A", "A", "D", "D"]
    ]
    return general.get_cells_from_strings_2(strings, 320, 160, 160, 80)


# cool loop
def get_cool_thing_5():
    strings = [
        ["D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "A", "A", "A", "D", "D", "D"],
        ["D", "D", "D", "A", "D", "A", "D", "D", "D"],
        ["D", "D", "A", "D", "A", "D", "A", "D", "D"],
        ["D", "D", "A", "D", "A", "D", "A", "D", "D"],
        ["D", "D", "A", "D", "A", "D", "A", "D", "D"],
        ["D", "D", "D", "A", "D", "A", "D", "D", "D"],
        ["D", "D", "D", "A", "A", "A", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D"]
    ]
    return general.get_cells_from_strings_2(strings, 80, 80, 30, 30)



def get_cool_thing_6():
    strings = [
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "A", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "A", "A", "A", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "D", "A", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "D", "A", "D", "A", "A", "A", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "A", "D", "D", "D", "A", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "A", "D", "D", "D", "A", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "A", "D", "A", "D", "A", "D", "A", "D", "A", "D", "D", "D", "D", "D", "D", "D"],
        ["D", "D", "D", "D", "D", "A", "D", "A", "D", "A", "D", "A", "D", "D", "D", "D", "D", "D", "D", "D"]
    ]
    return general.get_cells_from_strings_2(strings, 160, 160, 50, 40)