# ── LOOPS ─────────────────────────────────
# Loops repeat code multiple times
# Without loops → you'd write same code 100x
# With loops → write once, run 100x! 🔥

# ── 1. FOR LOOP ───────────────────────────
# Used when you know HOW MANY times to repeat
# Used in: lists, data processing, games

# basic for loop
for i in range(5):
    print(i)          # prints 0,1,2,3,4

# range with start and end
for i in range(1, 6):
    print(i)          # prints 1,2,3,4,5

# range with steps
for i in range(0, 10, 2):
    print(i)          # prints 0,2,4,6,8

#let's put some DSA problem using for loop 

# ── 1. FIND MAXIMUM NUMBER IN LIST ────────
# Problem: find biggest number without max()
# Used in: sorting algorithms, data analysis

numbers = [34, 67, 23, 89, 12, 45]
maximum = numbers[0]      # assume first is biggest

for num in numbers:
    if num > maximum:
        maximum = num     # update if bigger found

print(f"Maximum: {maximum}")   # 89


# ── 2. COUNT OCCURRENCES ──────────────────
# Problem: how many times does 3 appear?
# Used in: search engines, data processing

numbers = [1, 3, 5, 3, 7, 3, 9, 3]
count = 0
target = 3

for num in numbers:
    if num == target:
        count += 1

print(f"{target} appears {count} times")   # 4 times

#this above two problem used in weather app ~ what is the highest temp of day etc.

'''
Find Maximum → any time you need 
               "who/what is the biggest/best/highest"

Count Occurrences → any time you need
                    "how many times does X appear" 
'''

# ── 3. REVERSE A STRING ───────────────────
# Problem: reverse "afroj" → "jorfa"
# Asked in almost EVERY coding interview!

name = "Joey"
reversed_name = ""

for char in name:
    reversed_name = char + reversed_name

print(f"Reversed: {reversed_name}")   # jorfa

name = "conrad"
reversed_name = ""

for char in name:
    reversed_name = char + reversed_name

print(f"Reversed: {reversed_name}")

'''
reverse a string ~ real world ex.
→ Encryption → reversing text to hide data
→ DNA research → reversing gene sequences
→ Undo feature → reverse last action
→ Palindrome check → needs reverse first!
→ URL shorteners → encode/decode links
'''

# ── 4. CHECK PALINDROME ───────────────────
# Problem: is "madam" same forwards/backwards?
# palindrome = reads same both ways
# Used in: string processing interviews

word = "madam"
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

if word == reversed_word:
    print(f"{word} is a palindrome! ")
else:
    print(f"{word} is not a palindrome! ")

# ── 5. SUM OF DIGITS ──────────────────────
# Problem: sum digits of 1234 → 1+2+3+4 = 10
# Asked in beginner coding interviews!

number = "1234"
total = 0

for digit in number:
    total += int(digit)

print(f"Sum of digits: {total}")   # 10

# ── 6. FIND DUPLICATES ────────────────────
# Problem: find numbers that appear twice
# Used in: data cleaning, databases

numbers = [1, 2, 3, 2, 4, 3, 5]
seen = []
duplicates = []

for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print(f"Duplicates: {duplicates}")   # [2, 3]

# ── 7. BUBBLE SORT ────────────────────────
# Problem: sort list from smallest to biggest
# Classic DSA sorting algorithm!
# Used in: databases, search results

numbers = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            # swap them!
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(f"Sorted: {numbers}")   # [11, 12, 22, 25, 34, 64, 90]

# ── 8. FIBONACCI SEQUENCE ─────────────────
# Problem: print first 10 fibonacci numbers
# 0,1,1,2,3,5,8,13,21,34...
# Used in: mathematics, nature patterns, DSA!

a = 0
b = 1

print("Fibonacci sequence:")
for i in range(21):
    print(a, end=" ")
    a, b = b, a + b   # swap trick!
    #this [a, b = b, a + b] is a trick called "Tuple Unpacking", python calculates the entire right side first then assigns the values. 
    # 0, 1, (0 + 1)1, (1 + 1)2, (2 + 1)3, .... so first two digit would be always a, b then third digit would be c that is ~ a + b = c... b+c = d... etc. 
print() 
#this print here is used for starting from new line

a, b = 0, 1
for i in range(10):
    print(f"{a} + {b} = {a + b}") # This shows the work!
    a, b = b, a + b

# ── WHILE LOOP ──────────────────
# while loop = keep going UNTIL condition false

# ── 1. BASIC WHILE ────────────────────────
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1        # without this = infinite loop!
    #count += 1 ~ without this it will keep print infinite loop like count: 1;

# ── 2. BREAK ──────────────────────────────
# exit loop completely when condition met

print("Break example:")
count = 0
while True:           # infinite loop!
    count += 1
    print(count)
    if count == 5: #Here used comparison operator - equal to, it is keep count till we reach at number 5 (strictly!)
        break         # stops at 5!


# ── 3. CONTINUE ───────────────────────────
# skip current iteration, keep going

print("Continue example:")
for i in range(10):
    if i % 2 == 0: #In this line i represent numbers 1, 2, 3, ... % symbol is modulus that shows remainder.If remainder = 0 it means even number.
        continue      # skip even numbers
    print(i)          # only prints odd: 1,3,5,7,9

# ── 4. PASS ───────────────────────────────
# does nothing! placeholder for future code
for i in range(5):
    if i == 3:
        pass          # will add code here later
    print(i)          # prints all numbers

# ── REAL WORLD EXAMPLES ───────────────────

# 1. ATM MACHINE
balance = 5000
while True:
    print(f"\nBalance: {balance}")
    amount = int(input("How much to withdraw? "))
    
    if amount > balance:
        print("Insufficient balance!")
        continue      # ask again!
    elif amount <= 0:
        print("Invalid amount!")
        continue
    else:
        balance -= amount
        print(f"Withdrawn! Remaining: {balance}")
        
    another = input("Another withdrawal? (yes/no): ")
    if another == "no":
        break         # exit ATM!

print("Thank you! Goodbye!")