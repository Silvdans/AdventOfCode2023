COLORS = {'green':13, 'red':12, "blue": 14}


file = "input.txt"

def parse_line(line : str):

    splited_line = line.split(':')
    index = int(splited_line[0].removeprefix('Game '))

    groups = splited_line[1].split(';')
    group_valid = True
    for group in groups:
        group = group.removeprefix(' ')
        group = group.removesuffix('\n')
        picks : list = group.split(', ')

        for pick in picks:
            number, color = pick.split(' ')
            if not int(number) <= COLORS[color]:
                group_valid = False
                break
    if group_valid:
        return index
    return 0

def algorithm(input):
    lines = input.readlines()
    sum : int = 0
    for line in lines:
        sum += parse_line(line)
    return sum

input = open(file)
print(algorithm(input))