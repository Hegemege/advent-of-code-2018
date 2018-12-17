
def main():
    # Part 1
    grid = get_grid(300, 8868)
    part_1(grid)

    # Part 2
    part_2(grid)


def get_grid(grid_size, register):
    return [[
        int(
            str(
                (
                    (i + 10) * j + register
                )
                * (i + 10)
                % 1000
            ).zfill(3)[0]
        ) - 5
        for i in range(1, grid_size + 1)] for j in range(1, grid_size + 1)]


def part_1(grid):
    # Part 1
    grid_size = len(grid)
    highest = float('-inf')
    highest_coord = None
    for y in range(grid_size - 2):
        for x in range(grid_size - 2):
            s = 0
            for j in range(3):
                for i in range(3):
                    s += grid[y + j][x + i]
            if s > highest:
                highest = s
                highest_coord = str(x+1) + ',' + str(y+1)

    print(highest_coord)


def part_2(grid):
    # Not very fast, but gets the solution in 2-3 minutes.
    # The search accelerates

    # Square sum is done with dynamic programming, where a X,Y -based square with size N
    # requires only 1 + N-1 + N-1 + 1 sum operations instead of the naive N*N
    # Could be made faster by caching the sum of each square size per axis when moving the square

    grid_size = len(grid)
    highest = float('-inf')
    highest_coords = None

    for y in range(grid_size):
        print('Row', y)
        for x in range(grid_size):
            square_sum = 0
            for square_size in range(1, 301 - max([x, y])):
                # Add the previous square sum
                local_sum = square_sum

                # Add the bottom right corner
                local_sum += grid[y + square_size - 1][x + square_size - 1]

                # Add the bottommost row and rightmost column
                for s in range(square_size - 1):
                    local_sum += grid[y + square_size - 1][x + s]
                    local_sum += grid[y + s][x + square_size - 1]

                if local_sum > highest:
                    highest = local_sum
                    highest_coords = str(x+1) + ',' + \
                        str(y+1) + ',' + str(square_size)

                # Set the square sum for the next square
                # that is 1 wider and 1 taller
                square_sum = local_sum

    print(highest_coords)


if __name__ == '__main__':
    main()
