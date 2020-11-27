from day3 import get_grid


def get_intersection_count(grid):
    return len([x for x in grid.values() if len(x) > 1])


def main(file_name):
    claims = [claim for claim in open(file_name)]
    grid = get_grid(claims)
    print(get_intersection_count(grid))


main('input.txt')


