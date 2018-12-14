

def main():
    input_data = list(map(lambda row: [row[5], row[36]], read_input()))

    # Part 1

    # Include all nodes mentioned
    unique_nodes = list(set(
        list(map(lambda x: x[1], input_data)) +
        list(map(lambda x: x[0], input_data))
    ))

    # Create lookup for nodes
    nodes = {}
    for node in unique_nodes:
        nodes[node] = []

    # Add requirements
    for requirement, node in input_data:
        nodes[node].append(requirement)

    order = ''

    while len(nodes) > 0:
        without_requirements = list(filter(
            lambda x: len(x[1]) == 0,
            list(nodes.items())
        ))

        choice = min(without_requirements, key=lambda x: x[0])[0]
        order += choice
        for k, v in nodes.items():
            if choice in v:
                v.remove(choice)
        nodes.pop(choice)

    print(order)


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
