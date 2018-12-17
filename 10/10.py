

def main():
    input_data = list(map(
        lambda x: list(map(
            int,
            list(filter(
                lambda y: len(y) > 0,
                x.replace('position=<', '')
                .replace('velocity=<', '')
                .replace('>', '')
                .replace(',', '')
                .split(' ')
            ))
        )),
        read_input()
    ))

    # Part 1 and 2
    points = input_data
    time = 0

    while True:
        time += 1
        # Move the points
        for point in points:
            point[0] += point[2]
            point[1] += point[3]

        # Check if it's in a tight enough bundle
        if debug_print(points) == True:
            action = input('Time: ' + str(time) +
                           '. Type c to continue or anything else to stop: ')
            if action == 'c':
                continue
            else:
                break


def debug_print(points):
    # Get the bounding box of the points. If it's too large, do not print anything
    minx = min(points, key=lambda x: x[0])[0]
    miny = min(points, key=lambda x: x[1])[1]
    maxx = max(points, key=lambda x: x[0])[0]
    maxy = max(points, key=lambda x: x[1])[1]

    if maxx - minx > 200 or maxy - miny > 200:  # Arbitrary
        #print("Too sparse to print:", maxx - minx, maxy - miny)
        return False

    # Create a grid and fill it
    grid = [['.' for i in range(maxx - minx + 1)]
            for j in range(maxy - miny + 1)]
    for point in points:
        x = point[0]
        y = point[1]
        grid[y - miny][x - minx] = '#'

    for j in range(len(grid)):
        print(''.join(grid[j]))

    return True


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
