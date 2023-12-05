file = 'input.txt'
def make_lists(lines):
    sum = 0
    for line in lines:
        split = line.split(': ')
        number = int(split[0].removeprefix('Card '))
        numbers, pool = split[1].split('|')
        list_number = [int(x) for x in numbers.split(' ') if x != '']
        list_pool = [int(x) for x in pool.split(' ') if x != '']
        inter = intersection(list_number, list_pool)
        value = 0 if len(inter) == 0 else 2 ** (len(inter) - 1)
        sum += value
    return sum

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def algorithm(input):
    lines = input.readlines()
    sum : int = 0
    liste = make_lists(lines)
    return liste

input = open(file)
print(algorithm(input))
