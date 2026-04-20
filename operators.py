# ── OPERATORS IN PYTHON ───────────────────
# Operators are symbols that perform 
# operations on variables and values

# ── 1. ARITHMETIC OPERATORS ───────────────
a = 10
b = 3

print(a + b)   # 13  → addition
print(a - b)   # 7   → subtraction
print(a * b)   # 30  → multiplication
print(a / b)   # 3.3333 → division (always float)
print(a // b)  # 3   → floor division (removes decimal)
print(a % b)   # 1   → modulus (remainder)
print(a ** b)  # 1000 → power (10³)

#after run you can see this on output panel or type python + file name in your terminal and you will see the number output. 

# ── 2. COMPARISON OPERATORS ───────────────
# These compare two values
# Result is always True or False (Boolean!)

a = 10
b = 3

print(a == b)   # False → equal to
print(a != b)   # True  → not equal to
print(a > b)    # True  → greater than
print(a < b)    # False → less than
print(a >= b)   # True  → greater or equal
print(a <= b)   # False → less or equal

# Every comparison returns True or False!
is_greater = a > b
print(is_greater)  # True

is_equal = a == b
print(is_equal)    # False

# ── 3. LOGICAL OPERATORS ──────────────────
# AND, OR, NOT — same as Discrete Math! 

print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Real example:
age = 18
has_id = True

print(age >= 18 and has_id)  # True → can enter!
print(age >= 18 or has_id)   # True
print(not has_id)             # False