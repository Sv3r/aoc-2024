def read_text_file(name):
    text_file = name + ".txt"
    with open(text_file) as file:
        content = file.read().splitlines()
    return content

def parse_input(filename):
    input_file = read_text_file(filename)
    reports = [x.split() for x in input_file]
    return reports

def sign(x):
    return (x > 0) - (x < 0)

def is_safe(report):
    differences = [int(report[i]) - int(report[i + 1]) for i in range(len(report) - 1)]
    return all(abs(difference) <= 3 and sign(differences[0]) == sign(difference) for difference in differences)

def part1(reports):
    return sum(1 for report in reports if is_safe(report))

def is_safe_with_tolerance(report):
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)) or is_safe(report))

def part2(reports):
    return sum(is_safe_with_tolerance(report) for report in reports)

def main():
    parsed_input = parse_input("input")
    print("Part 1:", part1(parsed_input))
    print("Part 2:", part2(parsed_input))

if __name__ == "__main__":
    main()