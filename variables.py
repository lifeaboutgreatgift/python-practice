#let's start with how to do comment in python then we will move to variables in this file.
#this hashtag is used for single line comment in python.

"""
Hii, this is a multi line
comment you can write as much you need under it.
comment used for explaination, todo future work and disable the code.
"""

#Now let's move to var 
"""
so Variable a memory unit like a container that hold data value.
variable_name = value
int is -1 , 2 (integers num)
float is real num  9.99 (decimal num)
use underscore _ to separate words in var name.
"""
price = 9.99
apple = 2
player_cassie = 0

#Now a char is single character (for example: b, ., &, 1, 6, T,etc.)
# the string type is a speacial type that consists of multi chars.
#it is in value side in variable usually to text.
me = 'I am learning coding'
quote = "jack of all trades, master of none, but oftentimes better than a master of one!"

print(f"Price: {price}, Apple: {apple}, Player: {player_cassie}, Message: {me}, Message: {quote}")

# ── USER INPUT ──────────────────────────
# input() always returns a string by default
# to convert it to number we use int() or float()

name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("Your height in cm? "))

print(f"Hi {name}! You are {age} years old and {height}cm tall.")

#input doesn't work! you need to input in  terminal or output section where it can receive input, it's a way you can put input in it.

# ── TYPE CONVERSION ──────────────────────
# changing one data type to another
num_string = "25"        # this is a string "25"
num_int = int(num_string)  # now it's integer 25
num_float = float(num_string)  # now it's float 25.0

print(type(num_string))  # <class 'str'>
print(type(num_int))     # <class 'int'>
print(type(num_float))   # <class 'float'>

# ── BOOLEAN ──────────────────────────────
# only two values - True or False
# used for yes/no, on/off, correct/wrong situations
is_student = True
is_working = False
has_github = True

print(f"Student: {is_student}, Working: {is_working}, GitHub: {has_github}")
