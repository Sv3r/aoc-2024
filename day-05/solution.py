import re

def read_text_file(filename):
    with open(f"{filename}.txt", 'r') as file:
        return file.read().split("\n\n")

def parse_file(file):
    rules = re.findall(r"(\d+)\|(\d+)", file[0])
    return (
        [(int(x), int(y)) for x, y in rules],
        [list(map(int, update.split(','))) for update in file[1].splitlines()]
    )

def part1(parsed_file):
    correct_updates = []
    for update in parsed_file[1]:
        if all(rule[0] not in update or rule[1] not in update or update.index(rule[0]) < update.index(rule[1])
                for rule in parsed_file[0]):
            correct_updates.append(update)

    return sum(update[len(update)//2] for update in correct_updates)

def compare_pages(x, y, rules):
    return -1 if (x, y) in rules else 1 if (y, x) in rules else 0

def part2(parsed_file):
    total = 0
    for update in parsed_file[1]:
        sorted_update = sorted(update, key=lambda page: [compare_pages(page, other_page, parsed_file[0]) for other_page in update])
        if sorted_update != update:
            total += sorted_update[len(sorted_update) // 2]
    return total

def main():
    input_file = read_text_file("input")
    parsed_file = parse_file(input_file)
    print("Part 1:", part1(parsed_file))
    print("Part 2:", part2(parsed_file))

if __name__ == "__main__":
    main()