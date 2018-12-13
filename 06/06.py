import math
import string
import random


def main():
    input_data = list(map(
        lambda row: list(map(int, row.split(', '))),
        read_input()
    ))

    minx = min(input_data, key=lambda x: x[0])[0]
    maxx = max(input_data, key=lambda x: x[0])[0]
    miny = min(input_data, key=lambda x: x[1])[1]
    maxy = max(input_data, key=lambda x: x[1])[1]

    width = maxx - minx + 1
    height = maxy - miny + 1

    # Remap the corrdinates to be 0-based
    points = list(map(lambda x: [x[0] - minx, x[1] - miny], input_data))
    grid = [[0 for i in range(width)] for j in range(height)]

    # Part 1

    # Assumption: if a grid's edge is closest to a point A, then the area
    # point A covers is infinite. Or if A is on the edge

    # Iterate through the grid and calculate distance to every point.
    # Store the coordinates of the one that is closest, or None on tie
    for j in range(height):
        for i in range(width):
            closest = math.inf
            closest_point = None
            for p in points:
                distance = abs(p[0] - i) + abs(p[1] - j)
                if distance < closest:
                    closest = distance
                    closest_point = p
                elif distance == closest:
                    closest_point = None
            grid[j][i] = closest_point

    # Go around the edges and remove those closest to the edge from the points
    for j in range(height):
        for i in range(width):
            if i > 0 and j > 0 and i < width - 1 and j < height - 1:
                continue

            if grid[j][i] in points:
                points.remove(grid[j][i])

    flatgrid = [item for sublist in grid for item in sublist]
    # Get the point that has the most occurances in flatgrid,
    # and get the amount of those occurances, including the original
    # point itself
    print(flatgrid.count(max(points, key=lambda p: flatgrid.count(p))))

    # Part 2

    points = list(map(lambda x: [x[0] - minx, x[1] - miny], input_data))
    grid = [[False for i in range(width)] for j in range(height)]
    for j in range(height):
        for i in range(width):
            total_distance = sum(map(
                lambda p: abs(p[0] - i) + abs(p[1] - j),
                points
            ))
            if total_distance < 10000:
                grid[j][i] = True

    flatgrid = [item for sublist in grid for item in sublist]
    print(sum(flatgrid))


def debug(width, height, grid, points):
    symbols = string.ascii_lowercase + string.ascii_uppercase
    random.shuffle(symbols)
    lookup = {}
    for i in range(len(points)):
        lookup[tuple(points[i])] = symbols[i]

    for j in range(height):
        for i in range(width):
            point = grid[j][i]
            if point is None:
                print('.', end='')
            else:
                t = tuple(point)
                if t in lookup:
                    print(lookup[t], end='')
                else:
                    print('.', end='')
        print('')


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
