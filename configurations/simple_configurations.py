from configurations import general


def get_test_1(x, y):
    points = [(1, 1), (1, 3), (2, 2), (2, 4), (3, 3), (3, 4), (4, 2), (4, 4), (5, 1), (5, 3), (2, 5), (4, 5)]
    return general.get_cells_with_points(x, y, points, 20, 20)


def get_test_2():
    points = [(0,2),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(5,0),(5,2),(5,4)]
    return general.get_cells_with_points(100, 50, points, 40, 20)

# cool looping thing
def get_test_3():
    points = [(0,1),(0,5),(1,0),(2,0),(2,1),(2,5),(3,0),(1,3),(2,2),(2,3),(2,4),(3,3),(1,6),(2,6),(3,6),(4,1),(4,5)]
    return general.get_cells_with_points(100, 50, points, 40, 20)

def get_test_4():
    points= [(),(),(),()]
    return general.get_cells_with_points(100, 50, points, 40, 20)