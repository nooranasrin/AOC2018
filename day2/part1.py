from functools import reduce


def count_letters(letter_count, box_id):
    characters = list(box_id)
    repetition = []
    for character in characters:
        count = characters.count(character)
        if count not in repetition and (count == 2 or count == 3):
            letter_count[str(count)] = letter_count[str(count)] + 1
            repetition.append(count)
    return letter_count


def calculate_check_sum(box_ids):
    letter_count = {"2": 0, "3": 0}
    letter_count = reduce(count_letters, box_ids, letter_count)
    return letter_count["2"] * letter_count["3"]


def main():
    box_ids = [box_id.strip() for box_id in open("input.txt")]
    check_sum = calculate_check_sum(box_ids)
    print(check_sum)


main()
