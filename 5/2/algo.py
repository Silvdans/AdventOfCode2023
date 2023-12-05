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

def get_result(seeds, others_list):
    locations = []
    for seed in seeds:
        
        tmp_seed = seed
        for group in others_list:
            for index in range(0, len(group), 3):
                result = get_target_number(group[index], group[index+1], group[index+2], tmp_seed)
                if result:
                    tmp_seed = result
                    break
        locations.append(result) if result else locations.append(tmp_seed)
    return locations
        
def get_target_number(destination, source, _range, seed):
    if source <= seed <= source + _range:
        index = seed - source
        return index + destination

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