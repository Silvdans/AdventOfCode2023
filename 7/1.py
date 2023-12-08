from collections import Counter

def is_five_of_a_kind(hand):
    return len(set(hand)) == 1 and len(hand) == 5

def is_four_of_a_kind(hand):
    counts = Counter(hand)
    if any(count == 4 for count in counts.values()) and len(set(hand)) <= 2:
        return dict(counts)
    else:
        return None

def is_full_house(hand):
    counts = Counter(hand)
    if any(count == 3 for count in counts.values()) and any(count == 2 for count in counts.values()) and len(set(hand)) == 2:
        return dict(counts)
    else:
        return None
def is_three_of_a_kind(hand):
    counts = Counter(hand)
    if any(count == 3 for count in counts.values()) and len(set(hand)) <= 3:
        return dict(counts)
    else:
        return None

def is_two_pair(hand):
    counts = Counter(hand)
    if sum(count == 2 for count in counts.values()) == 2 and len(set(hand)) <= 3:
        return dict(counts)
    else:
        return None

def is_one_pair(hand):
    counts = Counter(hand)
    if sum(count == 2 for count in counts.values()) == 1 and len(set(hand)) <= 4:
        return dict(counts)
    else:
        return None

def is_high_card(hand):
    return len(set(hand)) == 5

def sort_dict_by_value(input_dict):

    sorted_items = sorted(input_dict.items(), key=lambda x: x[1])  # Extract the keys from the sorted itemsreverse()
    sorted_items.reverse()
    sorted_keys = [item[0] for item in sorted_items]

    return sorted_keys

file = 'input.txt'

map_values = {
    "A":14,
    "K":13,
    "Q":12,
    "J":11,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
}
def parse_values_in_collection(lines):
    table = []
    for line in lines:
        cards, bid = line.split(' ')
        bid = bid.removesuffix('\n')
        table.append((cards, int(bid)))
    return table

def get_uniques_values(char: str):
    return list(set(char))

def get_force(card : str):
    one = is_five_of_a_kind(card)
    if one:
        return 700000 + map_values[card[0]]

    two = is_four_of_a_kind(card)
    if two:
        counter = sort_dict_by_value(two)
        return 600000 + 100 * map_values[counter[0]] + map_values[counter[1]]
    
    four = is_full_house(card)
    if four:
        counter = sort_dict_by_value(four)
        return 500000 + 100 * map_values[counter[0]] + map_values[counter[1]]

    three = is_three_of_a_kind(card)
    if three:
        counter = sort_dict_by_value(three)
        return 400000 + 200 * map_values[card[0]] + 300 * map_values[card[1]] + 100 * map_values[card[2]]

    five = is_two_pair(card)
    if five:
        counter = sort_dict_by_value(five)
        return 300000 + 100 * map_values[card[0]] + 1100 * map_values[card[1]] + 100 * map_values[card[2]]

    six = is_one_pair(card)
    if six:
        counter = sort_dict_by_value(six)
        return 200000 + (100 * map_values[counter[0]]) + map_values[counter[1]] + map_values[counter[2]] + map_values[counter[3]]
    
    else:
        return 100000 + map_values[card[0]] + map_values[card[1]] + map_values[card[2]] + map_values[card[3]] + map_values[card[4]]        
    
def solve(table):
    forces = []
    for card, bid in table:
        forces.append((get_force(card), bid))

    sorted_forces = sorted(forces, key=lambda x: x[0])
    sum = 0
    for index, item in enumerate(sorted_forces):
        sum += (index+1) * item[1]

    print(sum)
    print("a")

def algorithm(input):
    lines = input.readlines()
    table = parse_values_in_collection(lines)
    result = solve(table)
    return result

input = open(file)
print(algorithm(input))