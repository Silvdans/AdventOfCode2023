import re
from collections import defaultdict
file = 'input.txt'

def get_seeds(lines):
    for line in lines:
        nb_list = line.removeprefix('seeds: ')
        nb_list = nb_list.removesuffix('\n')
        seeds = nb_list.split(' ')
        return [int(x) for x in seeds]
    
def get_other_list():
    input = open(file)
    next(input)
    next(input)
    append_list = []
    a = input.read().split(':')
    for line in a:
        pattern = re.compile(r'[^0-9\s]')
        result = pattern.sub('', line)
        result = re.sub(r'\n', ' ', result)
        result = result.split(' ')
        result = list(filter(None, result))
        append_list.append([int(x) for x in result])
        
    return append_list
def change_list(liste):
    return list(zip(liste[::2], liste[1::3]))
    
def get_result(seeds, others_list):
    locations = []
    seeds = change_list(seeds)
    for seed, range_seed in seeds:
        
        high_seed = range_seed - seed
        low_seed = seed
        for group in others_list:
            overlap = []
            range_destination_list = []
            for index in range(0, len(group), 3):
                destination, source, _range = group[index], group[index+1], group[index+2],
                D = destination - source
                end = source + _range

                if not(end < low_seed or source > high_seed):
                    overlap.append((max(source, low_seed), min(end, high_seed), D))
            for i, interval in enumerate(overlap):
                low, high , D = interval
                range_destination_list.append((low + D, high + D))
                if(i < len(overlap) -1 and overlap[i+1][0] > high + 1):
                    range_destination_list.append((high + 1, overlap[i+1][0] - 1))

            if len(range_destination_list) == 0:
                range_destination_list.append(seed, high_seed)

    return locations  
    
def algorithm(input):
    lines = input.readlines()
    sum : int = 0
    seeds = get_seeds(lines)
    input.close()
    others_list = get_other_list()

    result = get_result(seeds, others_list)
    print(min(result))
    


    return sum

input = open(file)

algorithm(input)