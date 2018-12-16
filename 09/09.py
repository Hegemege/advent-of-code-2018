from collections import deque


class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous


def main():
    input_data = read_input()[0].split(' ')
    player_count = int(input_data[0])
    marble_count = int(input_data[6])

    players = [0 for i in range(player_count)]
    marbles = deque(Node(i, None, None) for i in range(marble_count + 1))

    # Part 1

    play(players, marbles)
    print(max(players))

    # Part 2

    marble_count *= 100
    players = [0 for i in range(player_count)]
    marbles = deque(Node(i, None, None) for i in range(marble_count + 1))
    play(players, marbles)
    print(max(players))


def play(players, marbles):
    root = marbles.popleft()
    root.next = root
    root.previous = root
    current_marble = root
    player_index = 0

    # Part 1

    while len(marbles) > 0:
        # Player places the next marble
        new_marble = marbles.popleft()

        if new_marble.value % 23 != 0:
            # Get a reference of the next marble and insert the new marble
            next_marble = current_marble.next

            next_marble.next.previous = new_marble
            new_marble.next = next_marble.next
            next_marble.next = new_marble
            new_marble.previous = next_marble

            current_marble = new_marble

        # Player scores points
        else:
            # The to-be-placed marble
            players[player_index] += new_marble.value

            # And collect the marble 7 places back
            # ¯\_(ツ)_/¯
            collect_marble = current_marble.previous.previous.previous.previous.previous.previous.previous

            collect_marble.previous.next = collect_marble.next
            collect_marble.next.previous = collect_marble.previous

            players[player_index] += collect_marble.value
            current_marble = collect_marble.next

        #debug(root, player_index, current_marble)

        player_index = (player_index + 1) % len(players)


def debug(root, player_index, current_marble):
    print('[' + str(player_index) + '] ', end='')
    if root is current_marble:
        print('(' + str(root.value) + ')', end='')
    else:
        print(' ' + str(root.value) + ' ', end='')

    current = root.next
    while current is not root:
        if current is current_marble:
            print('(' + str(current.value) + ')', end='')
        else:
            print(' ' + str(current.value) + ' ', end='')
        current = current.next
    print('')


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
