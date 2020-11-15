def get_first_repeated_frequency(frequency_changes, visited_frequencies):
    current_frequency = visited_frequencies[len(visited_frequencies) - 1]
    while 1:
        for change in frequency_changes:
            current_frequency = current_frequency + change
            if current_frequency in visited_frequencies:
                return current_frequency
            visited_frequencies.append(current_frequency)


def main():
    frequency_changes = [int(line) for line in open("input.txt")]
    visited_frequencies = [0]
    repeated_frequency = get_first_repeated_frequency(frequency_changes, visited_frequencies)
    print(repeated_frequency)


main()
