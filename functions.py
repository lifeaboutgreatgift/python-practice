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