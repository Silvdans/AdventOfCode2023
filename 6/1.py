import numpy 
file = 'input.txt'

def parse_tables(lines):

    time_list = [int(x) for x in lines[0].removeprefix('Time:        ').removesuffix('\n').split(' ') if x.isdigit()]
    distance_list = [int(x) for x  in lines[1].removeprefix('Distance:   ').removesuffix('\n').split(' ') if x.isdigit()]
    final_table = list(zip(time_list[::1], distance_list[::1]))
    return final_table

def solve(table : tuple):
    
    final_list = []
    for t_max, best_record_distance in table:
        distance_list = []
        for v in range(0, t_max + 1):
            t = t_max - v
            distance = t * v
            distance_list.append(distance)
        nb_run = len([x for x in distance_list if x > best_record_distance])
        final_list.append(nb_run)
    return numpy.prod(final_list)

def algorithm(input):
    lines = input.readlines()
    table = parse_tables(lines)
    result = solve(table)
    return result

input = open(file)
print(algorithm(input))