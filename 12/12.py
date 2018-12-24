

class Node:
    def __init__(self, value, index, next, previous):
        self.value = value
        self.next_value = value
        self.index = index
        self.next = next
        self.previous = previous


def main():
    input_data = read_input()
    initial_row = input_data.pop(0)  # Extract the initial state
    input_data.pop(0)  # Remove the empty row
    rules = list(map(lambda x: x.split(" => "), input_data))
    initial_row = initial_row[15:]

    # Build the initial state
    current = None
    for i in range(len(initial_row)):
        previous = None
        if current is not None:
            previous = current

        current = Node(initial_row[0], i, None, None)
        initial_row = initial_row[1:]

        if previous is not None:
            previous.next = current
            current.previous = previous

    # When growing - add 3 more to both ends, and in the end remove the non-grown nodes from both ends
    # Current node is always some node in the hierarchy
    generation_number = 0
    #debug(current, True, True)
    for i in range(20):
        generation_number += 1
        current = grow(current, rules)
        #debug(current, True, True)

    leftmost = get_leftmost(current)
    index_sum = 0
    while leftmost is not None:
        if leftmost.value == '#':
            index_sum += leftmost.index
        leftmost = leftmost.next

    print(index_sum)


def grow(node, rules):
    '''Take the current state described by one node'''
    # Find the leftmost node and add the 3 nodes
    leftmost = get_leftmost(node)
    for i in range(3):
        new_node = Node('.', leftmost.index - 1, None, None)
        leftmost.previous = new_node
        new_node.next = leftmost
        leftmost = new_node

    # Find the rightmost and add 3 nodes
    rightmost = get_rightmost(node)
    for i in range(3):
        new_node = Node('.', rightmost.index + 1, None, None)
        rightmost.next = new_node
        new_node.previous = rightmost
        rightmost = new_node

    # Go through the nodes and test all rules
    current = leftmost.next.next
    while current.next.next is not None:
        pp = current.previous.previous
        p = current.previous
        n = current.next
        nn = current.next.next
        for rule in rules:
            if rule[0][0] == pp.value and rule[0][1] == p.value and rule[0][2] == current.value and rule[0][3] == n.value and rule[0][4] == nn.value:
                current.next_value = rule[1]
            # Assumes that every combination is in the rules
        current = current.next

    # Remove the ungrown nodes from both ends
    leftmost = get_leftmost(node)
    while leftmost.next_value == '.':
        leftmost.next.previous = None
        leftmost = leftmost.next

    rightmost = get_rightmost(leftmost)
    while rightmost.next_value == '.':
        rightmost.previous.next = None
        rightmost = rightmost.previous

    # Finally update the state for all nodes
    current = get_leftmost(rightmost)
    while current is not None:
        current.value = current.next_value
        current = current.next

    return rightmost  # Return any valid node - in this case rightmost was updated last


def get_leftmost(node):
    leftmost = node
    while leftmost.previous is not None:
        leftmost = leftmost.previous
    return leftmost


def get_rightmost(node):
    rightmost = node
    while rightmost.next is not None:
        rightmost = rightmost.next
    return rightmost


def debug(node, p, n):
    if p and node.previous is not None:
        debug(node.previous, True, False)

    print(node.value, end="")

    if n and node.next is not None:
        debug(node.next, False, True)


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
