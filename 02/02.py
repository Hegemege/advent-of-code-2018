

def main():
    input_data = read_input()
    data = list(map(letter_frequencies, input_data))

    # Part 1
    twos = sum([1 for x in data if 2 in x])
    threes = sum([1 for x in data if 3 in x])
    print(twos * threes)

    # Part 2
    id_length = len(input_data[0])  # All ids are the same length
    # Slow N^2 search
    for id in input_data:
        for id_comp in input_data:
            if id == id_comp:
                continue
            common_letters = [id[i]
                              for i in range(id_length) if id[i] == id_comp[i]]
            if len(common_letters) == id_length - 1:
                print(''.join(common_letters))
                return


def letter_frequencies(id):
    letter_count = {}
    for letter in id:
        if letter not in letter_count.keys():
            letter_count[letter] = 0
        letter_count[letter] += 1

    frequencies = {}
    for k, v in letter_count.items():
        if v not in frequencies:
            frequencies[v] = []
        frequencies[v].append(k)

    return frequencies


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
