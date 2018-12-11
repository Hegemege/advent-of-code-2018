

def main():
    input_data = read_input()

    # Part 1
    fabric_size = 1000
    fabric = [[[] for y in range(fabric_size)] for x in range(fabric_size)]

    non_overlapping_ids = set()

    for claim in input_data:
        id, claim = claim.split(' @ ')
        position, claim = claim.split(": ")
        x, y = map(int, position.split(','))
        w, h = map(int, claim.split('x'))
        non_overlapping_ids.add(id)
        for i in range(w):
            for j in range(h):
                square = fabric[x + i][y + j]
                for existing_claim in square:
                    if existing_claim in non_overlapping_ids:  # I wish there was a better way
                        non_overlapping_ids.remove(existing_claim)
                if len(square) > 0:
                    if id in non_overlapping_ids:
                        non_overlapping_ids.remove(id)
                square.append(id)

    print(sum(map(lambda x: sum(map(lambda c: 1, filter(lambda y: len(y) > 1, x))), fabric)))

    # Part 2

    print(non_overlapping_ids)


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
