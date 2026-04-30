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


# Write a program that calculates the factorial of a number

def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers.')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    factorial_input = input('Enter a non-negative integer to compute its factorial: ').strip()
    if not factorial_input:
        print('No input provided for factorial.')
    else:
        try:
            number = int(factorial_input)
            print(factorial(number))
        except ValueError as exc:
            print(f'Invalid input: {exc}')