
class Node:
    def __init__(self, data, depth):
        children_count = int(data.pop(0))
        metadata_count = int(data.pop(0))

        self.children = []
        self.metadata = []
        self.depth = depth

        for i in range(children_count):
            self.children.append(Node(data, depth + 1))

        for i in range(metadata_count):
            self.metadata.append(int(data.pop(0)))

    def sum(self):
        return sum(map(lambda x: x.sum(), self.children)) + sum(self.metadata)

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        return sum(map(
            lambda x:
                self.children[x - 1].value()
                if (x > 0 and x <= len(self.children))
                else 0,
            self.metadata
        ))

    def __repr__(self):
        rep = ('- ' * self.depth) + 'v' + str(self.value()) + ' c' + \
            str(len(self.children)) + ' - ' + \
            ' '.join(map(str, self.metadata)) + '\n'
        for child in self.children:
            rep += child.__repr__()

        return rep


def main():
    input_data = read_input()[0].split(' ')

    tree = Node(input_data, 0)

    # Part 1

    print(tree.sum())

    # Part 2

    print(tree.value())


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
