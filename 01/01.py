
def main():
    data = read_input()
    # Part 1
    print(sum(map(lambda x: int(x), data)))

    # Part 2
    seen_frequencies = set()
    current_frequency = 0
    while True:
        for item in data:
            current_frequency += int(item)
            if current_frequency in seen_frequencies:
                print(current_frequency)
                return
            seen_frequencies.add(current_frequency)


# Read the file and remove trailing new line characters
def read_input():
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
