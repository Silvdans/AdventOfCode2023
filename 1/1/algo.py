file = 'input.txt'

def last_digit_of_string(input_string):
    """
    Returns the last digit of a given string.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - int: The last digit of the string, or None if no digit is found.
    """
    for char in reversed(input_string):
        if char.isdigit():
            return int(char)
    return None

def first_digit_of_string(input_string):
    """
    Returns the last digit of a given string.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - int: The last digit of the string, or None if no digit is found.
    """
    for char in input_string:
        if char.isdigit():
            return int(char)
    return None

def algorithm(input):
    lines = input.readlines()
    sum : int = 0
    for line in lines:
        num1 = first_digit_of_string(line)
        num2 = last_digit_of_string(line)
        concatenated_result = int(str(num1) + str(num2))
        sum += concatenated_result
    return sum

input = open(file)
print(algorithm(input))
