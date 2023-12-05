file = "input.txt"

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def check_word(input_string, index, char : str, reversed = False) -> int | None:
   
    if char.isalpha():
        word = char
        num = 1
        for _ in range(4):
            if (index + num) >= len(input_string):
                return None
            word = word + input_string[index + num]
            if word in numbers:
                return numbers.index(word) + 1
            num += 1
    return None

def check_word_inversed(input_string, index, char : str) -> int | None:
   
    if char.isalpha():
        word = char
        num = 1
        for _ in range(4):
            if (index - num) < 0:
                return None
            word = word + input_string[index - num]
            if word in numbers:
                return numbers.index(word) + 1
            num += 1
    return None
    

def last_digit_of_string(input_string):
    """
    Returns the last digit of a given string.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - int: The last digit of the string, or None if no digit is found.
    """
    for index, char in enumerate(input_string[::-1]):
        if char.isdigit():
            return int(char)
        else:
            word = check_word_inversed(input_string[::-1], index, char)
            if word:
                return word
    return None

def first_digit_of_string(input_string):
    """
    Returns the last digit of a given string.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - int: The last digit of the string, or None if no digit is found.
    """
    for index, char in enumerate(input_string):
        if char.isdigit():
            return int(char)
        else:
            word = check_word(input_string, index, char)
            if word:
                return word
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