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
    print(f"{word} is a palindrome! ✅")
else:
    print(f"{word} is not a palindrome! ❌")

