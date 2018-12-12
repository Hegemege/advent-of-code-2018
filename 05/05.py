from functools import reduce
import string
import math


def main():
    input_data = read_input()[0]

    # Part 1
    result = react(input_data)
    print(len(result))

    # Part 2
    shortest = math.inf
    for element in string.ascii_lowercase:
        polymer = input_data.replace(element, '').replace(element.upper(), '')
        result = react(polymer)
        if len(result) < shortest:
            shortest = len(result)
    print(shortest)


def react(polymer):
    while True:
        current_length = len(polymer)

        # Using reduce, could be replaced with a more readable for-loop, but index problems might arise
        # A while loop would be the easiest to understand, maybe
        # ... and faster. Lots of lists being created here
        polymer = ''.join(
            reduce(
                lambda x, y:
                # First, we need to check if the current iteration has any content ([:-1] wont work)
                # Add the next element to the polymer of everything to the left of it has been
                # reacted with (or it starts the polymer)
                [y] if len(x) == 0 else (
                    # If the polarity check returns True, we remove the last element from the polymer,
                    # ignore the next element and pass the polymer to the next iteration
                    # If the polarity check returns False, we append the new element to the end
                    # (but because reduce doesn't deal with references, we just create a new list)
                    x[:-1] if polarity(x[-1], y) else add_and_return(x, y)
                ),
                polymer,
                []))
        if current_length == len(polymer):
            return polymer


def polarity(a, b):
    return a != b and (a.upper() == b or a.lower() == b)


def add_and_return(x, y):
    x.append(y)
    return x


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
