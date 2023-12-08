import math
file = 'input.txt'

def parse_tables(lines):

    time_list = "".join([x for x in lines[0].removeprefix('Time:        ').removesuffix('\n').split(' ') if x.isdigit()])
    distance_list = "".join([x for x  in lines[1].removeprefix('Distance:   ').removesuffix('\n').split(' ') if x.isdigit()])
    final_table = (int(time_list), int(distance_list))
    return final_table

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return None
    
def solve(table : tuple):
    
    t_max, best_record_distance = table
    
    a = -1
    b = t_max
    c = -best_record_distance
    
    result = solve_quadratic(a, b, c)
    return result

def algorithm(input):
    lines = input.readlines()
    table = parse_tables(lines)
    
    result = solve(table)
    result = math.ceil(result[1] - result[0])
    return result

input = open(file)


import time
start_time = time.time()
print(algorithm(input))
print("--- %s seconds ---" % (time.time() - start_time))