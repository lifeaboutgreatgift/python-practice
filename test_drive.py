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


# Write a program that generates a blog

import random

def generate_blog_post():
    titles = [
        "The Art of Coding",
        "Exploring Python",
        "Daily Life Hacks",
        "Tech Trends 2023",
        "My Journey in Programming"
    ]
    contents = [
        "In this post, we dive into the world of programming...",
        "Python is a versatile language that...",
        "Here are some useful tips for everyday life...",
        "The latest trends in technology include...",
        "Sharing my experiences and lessons learned..."
    ]
    title = random.choice(titles)
    content = random.choice(contents)
    return f"<h1>{title}</h1><p>{content}</p>"

if __name__ == '__main__':
    blog_input = input('Enter "generate" to create a blog post: ').strip().lower()
    if blog_input == 'generate':
        print(generate_blog_post())
    else:
        print('Invalid command.')