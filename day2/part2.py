import difflib


def find_common_letters_from_correct_boxes(box_ids):
    for current_id in box_ids:
        remaining_box_ids = box_ids[box_ids.index(current_id) + 1:]
        for box_id in remaining_box_ids:
            diff = [char for char in difflib.ndiff(current_id, box_id) if char[0] != ' ']
            if len(diff) == 2:
                return "".join([char.strip() for char in difflib.ndiff(current_id, box_id) if char[0] == ' '])


def main():
    box_ids = [box_id.strip() for box_id in open("input.txt")]
    common_letters = find_common_letters_from_correct_boxes(box_ids)
    print(common_letters)


main()
