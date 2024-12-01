def read_text_file(name):
    text_file = name + ".txt"
    with open(text_file) as file:
        content = file.read().splitlines()
    return content

def separate_lines(lines):
    left_list = []
    right_list = []

    for line in lines:
        split = line.split()
        left_list.append(int(split[0]))
        right_list.append(int(split[1]))

    left_list.sort()
    right_list.sort()

    return left_list, right_list

def main():
    input_file = read_text_file("input")

    separated = separate_lines(input_file)

    left_list = separated[0]
    right_list = separated[1]

    # total_distance = 0
    # for i in range(len(left_list)):
    #     distance = abs(left_list[i] - right_list[i])
    #     total_distance += distance

    # print(total_distance)

    similarity_score = 0
    for i in range(len(left_list)):
        right_count = right_list.count(left_list[i])
        similarity_score += left_list[i] * right_count

    print(similarity_score)

if __name__ == "__main__":
    main()