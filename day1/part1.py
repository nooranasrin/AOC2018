from functools import reduce


def find_total_frequency(current_frequency, change):
    return current_frequency + change


def main():
    frequency_changes = [int(line) for line in open('input.txt')]
    total_frequency = reduce(find_total_frequency, frequency_changes)
    print(total_frequency)


main()
