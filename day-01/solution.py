def read_text_file(name):
    text_file = name + ".txt"
    with open(text_file) as file:
        content = file.read().splitlines()
    return content

def separate_lines(lines):
    left_list = [int(x.split()[0]) for x in lines]
    right_list = [int(x.split()[1]) for x in lines]
    return left_list, right_list

def part1(separated):
    left_list = sorted(separated[0])
    right_list = sorted(separated[1])
    return sum(abs(left_list[i] - right_list[i]) for i in range(len(left_list)))

def part2(separated):
    left_list = separated[0]
    right_list = separated[1]
    return sum(left_list[i] * right_list.count(left_list[i]) for i in range(len(left_list)))

def main():
    input_file = read_text_file("input")
    separated = separate_lines(input_file)
    print("Part 1:", part1(separated))
    print("Part 2:", part2(separated))

if __name__ == "__main__":
    main()