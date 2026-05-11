import sys
sys.stdout.reconfigure(encoding='utf-8')

# ── FUNCTIONS ─────────────────────────────
# Function = reusable block of code
# Write once → use anywhere, anytime!
#
# Real life analogy:
# Function = recipe in a cookbook
# You write recipe once →
# cook it anytime you want! 😄
#
# Syntax:
# def function_name(parameters):
#     code here
#     return value

# ── 1. BASIC FUNCTION ─────────────────────
def greet():
    print("Hello! Welcome to Python!")

# calling the function
greet()        # Hello! Welcome to Python!
greet()        # same function, called again!
greet()        # and again! write once use many!

# ── 2. FUNCTION WITH PARAMETERS ───────────
# parameters = inputs to the function

def greet_person(name):
    print(f"Hello {name}! Welcome!")

greet_person("Jane")     # Hello Jane!
greet_person("Alex")      # Hello Alex!
greet_person("Dino")    # Hello Dino!

# ── 3. FUNCTION WITH RETURN ───────────────
# return = function gives back a value

def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")    # 8

def divide(a, b):
    return a / b

result = divide( 1728, 12)
print(f"1728 / 12 = {result}")

# ── 4. MULTIPLE PARAMETERS ────────────────
def calculate_grade(name, marks):
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"
    return f"{name} scored {marks} → Grade {grade}"

print(calculate_grade("Ava", 85))
print(calculate_grade("Aman", 92))
print(calculate_grade("Bob", 45))

# ── 5. DEFAULT PARAMETERS ─────────────────
# default = used when no value given

def greet_language(name, language="English"):
    if language == "English":
        print(f"Hello {name}!")
    elif language == "Hindi":
        print(f"Namaste {name}!")
    elif language == "Spanish":
        print(f"Hola {name}!")

greet_language("Aditi")              # uses default English
greet_language("Aditi", "Hindi")     # uses Hindi
greet_language("Aditi", "Spanish")   # uses Spanish

#learn more about it