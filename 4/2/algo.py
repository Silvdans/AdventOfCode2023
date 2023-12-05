def find_matching_numbers(list1, list2):
    """Return the intersection of two lists."""
    return [value for value in list1 if value in list2]

def generate_lists(lines):
    """Generate lists and calculate the sum based on specified conditions."""
    intersections = [find_matching_numbers(
        [int(x) for x in line.split(': ')[1].split('|')[0].split() if x != ''],
        [int(x) for x in line.split(': ')[1].split('|')[1].split() if x != '']
    ) for line in lines]

    count_list = [[len(x), 1] for x in intersections]

    for index, pack in enumerate(count_list):
        matching_numbers, copy = pack
        for _ in range(copy):
            i = index
            for _ in range(matching_numbers):
                if i >= len(count_list):
                    return sum(x[1] for x in count_list)
                count_list[i + 1][1] += 1
                i += 1

    return sum(x[1] for x in count_list)

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        result = generate_lists(lines)
    return result

if __name__ == "__main__":
    file_path = 'input.txt'
    print(main(file_path))
