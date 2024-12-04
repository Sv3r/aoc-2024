import re

def read_text_file(filename):
    with open(f"{filename}.txt", 'r') as file:
        return file.read().splitlines()

def get_horizontals(input_file):
    return [["".join(row), "".join(row)[::-1]] for row in input_file]

def get_verticals(input_file):
    return [["".join(column), "".join(column)[::-1]] for column in zip(*input_file)]

def get_diagonals(input_file):
    rows, cols = len(input_file), len(input_file[0])

    left_to_right = ["".join(input_file[row+i][i] for i in range(min(rows-row, cols))) for row in range(rows)] + \
                    ["".join(input_file[i][col+i] for i in range(min(rows, cols-col))) for col in range(1, cols)]

    right_to_left = ["".join(input_file[row + i][cols - 1 - i] for i in range(min(rows - row, cols))) for row in range(rows)] + \
                    ["".join(input_file[i][cols - 1 - col - i] for i in range(min(rows, cols - col))) for col in range(1, cols)]

    return left_to_right + [diagonal[::-1] for diagonal in left_to_right] + \
           right_to_left + [diagonal[::-1] for diagonal in right_to_left]

def part1(input_file):
    word = "XMAS"

    all_added = get_horizontals(input_file) + get_verticals(input_file) + [get_diagonals(input_file)]
    regex = r"(?=" + re.escape(word) + r")"

    return sum([sum([1 for _ in re.finditer(regex, string)]) for direction in all_added for string in direction])

def add_direction(row, col, direction):
    return row + direction[0], col + direction[1]

def check_x_mas(row, col, input_file):
    directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    values = []

    for direction in directions:
        new_row, new_col = add_direction(row, col, direction)
        if not (0 <= new_row < len(input_file) and 0 <= new_col < len(input_file[0])):
            return 0
        values.append(input_file[new_row][new_col])

    if any(value not in ['M', 'S'] for value in values):
        return 0

    upper_left, upper_right, bottom_right, bottom_left = values

    if (upper_left == 'M' and bottom_right != 'S') or (upper_left == 'S' and bottom_right != 'M'):
        return 0
    if (upper_right == 'M' and bottom_left != 'S') or (upper_right == 'S' and bottom_left != 'M'):
        return 0

    return 1

def part2(input_file):
    rows, cols = len(input_file), len(input_file[0])
    return sum(check_x_mas(row, col, input_file) for row in range(rows) for col in range(cols) if input_file[row][col] == 'A')

def main():
    input_file = read_text_file("input")
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))

if __name__ == "__main__":
    main()