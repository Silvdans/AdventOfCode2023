import numpy
file = 'input.txt'

def retrieve_symbols(input):
    string = input.read()
    symbol_list = []
    for char in string:
        if not char.isdigit() and char != '.':
            symbol_list.append(char)
    symbol_list = list(set(symbol_list))
    symbol_list.remove('\n')
    input.close()
    return symbol_list

def make_table(lines):
    table = []
    for line in lines:
        line = line.removesuffix('\n')
        table.append(line)
    return table

def is_number_adjacent_to_symbol(table, i, j, symbol_list):
    number = ''
    add_number = False
    tmp_j = j
    while table[i][j].isdigit():

        number += table[i][j]
        if j +1 < len(table[0]):
            j += 1 
        else:
            break
    
    for j in range(tmp_j, tmp_j+len(number)):
        if j-1 >= 0:
            if table[i][j-1] in symbol_list:
                add_number = True
                index_char = i, j-1
                break
            
        if j+1 < len(table[0]):
            if table[i][j+1] in symbol_list: 
                add_number = True
                index_char = i, j+1
                break
        if i-1 >= 0 and j-1 >= 0:
            if table[i-1][j-1] in symbol_list: 
                add_number = True
                index_char = i-1, j-1
                break
        if i-1 >= 0 :
            if table[i-1][j] in symbol_list:
                add_number = True
                index_char = i-1, j
                break
        if j+1 < len(table[0]) and i-1 >= 0:
            if table[i-1][j+1] in symbol_list:
                index_char = i-1, j+1
                add_number = True
                break
        if j-1 >= 0 and i+1 < len(table[0]):
            if table[i+1][j-1] in symbol_list:
                add_number = True
                index_char = i+1, j-1
                break
        if i+1 < len(table[0]):
            if table[i+1][j] in symbol_list:
                add_number = True
                index_char = i+1, j
                break
        if j+1 < len(table[0]) and i+1 < len(table[0]):
            if table[i+1][j+1] in symbol_list:
                add_number = True
                index_char = i+1, j+1
                break
    
    if add_number:
        return int(number), index_char
    return 0, None

def run_table(table, symbols_list : list):
    somme : int = 0
    order_char : dict = {}
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[i][j].isdigit():
                if j-1 < 0:
                    num, index_char = is_number_adjacent_to_symbol(table, i , j, symbols_list)
                    if index_char:
                        if not order_char.get(index_char):
                            order_char[index_char] = [num]
                        else:
                            order_char[index_char].append(num)
                    
                else:
                    if not table[i][j-1].isdigit():
                        num, index_char = is_number_adjacent_to_symbol(table, i , j, symbols_list)
                        if index_char:
                            if not order_char.get(index_char):
                                order_char[index_char] = [num]
                            else:
                                order_char[index_char].append(num)
                    else:
                        continue
                somme += num
    return somme, order_char

def calculate_result(order_char :dict):
    sum = 0
    for key, values in order_char.items():
        if len(values) == 2:
            sum += numpy.prod(values)
    return sum

input = open(file)
symbols = retrieve_symbols(input)

input = open(file)
table = make_table(input.readlines())
somme, order_char = run_table(table, symbols)

print(calculate_result(order_char))
