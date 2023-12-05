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
                break
            
        if j+1 < len(table[0]):
            if table[i][j+1] in symbol_list: 
                add_number = True
                break
        if i-1 >= 0 and j-1 >= 0:
            if table[i-1][j-1] in symbol_list: 
                add_number = True
                break
        if i-1 >= 0 :
            if table[i-1][j] in symbol_list:
                add_number = True
                break
        if j+1 < len(table[0]) and i-1 >= 0:
            if table[i-1][j+1] in symbol_list:
                add_number = True
                break
        if j-1 >= 0 and i+1 < len(table[0]):
            if table[i+1][j-1] in symbol_list:
                add_number = True
                break
        if i+1 < len(table[0]):
            if table[i+1][j] in symbol_list:
                add_number = True
                break
        if j+1 < len(table[0]) and i+1 < len(table[0]):
            if table[i+1][j+1] in symbol_list:
                add_number = True
                break
    if add_number:
        return int(number)
    return 0

def run_table(table, symbols_list : list):
    somme : int = 0
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[i][j].isdigit():
                if j-1 < 0:
                    num = is_number_adjacent_to_symbol(table, i , j, symbols_list)
                else:
                    if not table[i][j-1].isdigit():
                        num =  is_number_adjacent_to_symbol(table, i , j, symbols_list)
                    else:
                        continue
                somme += num
    return somme

input = open(file)
symbols = retrieve_symbols(input)

input = open(file)
table = make_table(input.readlines())
somme = run_table(table, symbols)
print(somme)
