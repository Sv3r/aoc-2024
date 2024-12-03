import re

def read_text_file(filename):
    with open(f"{filename}.txt", 'r') as file:
        return file.read().replace('\n', '')

def multiply(input_file, regex):
    return sum(int(match.group(1)) * int(match.group(2)) for match in re.finditer(regex, input_file))

def part1(input_file):
    regex = r"mul\((\d+),(\d+)\)"
    return multiply(input_file, regex)

def part2(input_file):
    regex = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    enabled, result = True, 0
    for match in re.finditer(regex, input_file):
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        elif enabled:
            result += int(match.group(1)) * int(match.group(2))

    return result

def main():
    input_file = read_text_file("input")
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))

if __name__ == "__main__":
    main()