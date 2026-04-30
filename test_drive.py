# Write a program that converts a Roman numeral to an integer
roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_int(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman.upper()):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total


if __name__ == '__main__':
    roman_input = input('Enter a Roman numeral: ').strip()
    if not roman_input:
        print('No input provided.')
    else:
        result = roman_to_int(roman_input)
        print(result)


