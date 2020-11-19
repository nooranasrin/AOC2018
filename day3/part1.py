import re


def get_intersections_count(claims):
    ids = {}
    for line in claims:
        id, row, column, width, height = map(int, re.findall(r'\d+', line))
        for y_coord in range(column, column + height):
            for x_coord in range(row, row + width):
                intersections = ids.get(str(f'({x_coord}, {y_coord})'), [])
                intersections.append(id)
                ids[str(f'({x_coord}, {y_coord})')] = intersections
    return len([x for x in ids.values() if len(x) > 1])


def main(file_name):
    claims = [claim for claim in open(file_name)]
    print(get_intersections_count(claims))


main('input.txt')


