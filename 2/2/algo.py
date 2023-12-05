import numpy 

COLORS = {'green':13, 'red':12, "blue": 14}



file = "input.txt"

def parse_line(line : str):
    MINIMUM = {'green':0, 'red':0, "blue":0}
    splited_line = line.split(':')
    index = int(splited_line[0].removeprefix('Game '))

    groups = splited_line[1].split(';')
    for group in groups:
        group = group.removeprefix(' ')
        group = group.removesuffix('\n')
        picks : list = group.split(', ')

        for pick in picks:
            number, color = pick.split(' ')
            if int(number) > MINIMUM[color]:
                MINIMUM[color] = int(number)
    for k, v in MINIMUM.items():
        if v == 0:
            del k
    a = numpy.prod(list(MINIMUM.values()))
    return a


def algorithm(input):
    lines = input.readlines()
    sum : int = 0
    for line in lines:
        sum += parse_line(line)
    return sum

input = open(file)
print(algorithm(input))