import re


def get_grid(claims):
    ids = {}
    for claim in claims:
        claim_id, row, column, width, height = map(int, re.findall(r'\d+', claim))
        for y_coord in range(column, column + height):
            for x_coord in range(row, row + width):
                intersections = ids.get(str(f'({x_coord}, {y_coord})'), [])
                intersections.append(claim_id)
                ids[str(f'({x_coord}, {y_coord})')] = intersections
    return ids
