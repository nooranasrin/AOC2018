import re
from day3 import get_grid


def get_not_intersected_claim_id(grid, claims):
    intersected_ids = set()
    all_ids = set()
    for claim in claims:
        claim_id, _, _, _, _ = map(int, re.findall(r'\d+', claim))
        for intersection, claim_ids in grid.items():
            if claim_id in claim_ids and len(claim_ids) > 1:
                intersected_ids.add(claim_id)
            else:
                all_ids.add(claim_id)
    return all_ids.difference(intersected_ids)


def main(file_name):
    claims = [claim for claim in open(file_name)]
    grid = get_grid(claims)
    print(get_not_intersected_claim_id(grid, claims).pop())


main('input.txt')
