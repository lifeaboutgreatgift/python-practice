# ── IF / ELSE CONDITIONS ───────────────────
# Used to make decisions in your program
# If this is true → do this
# Otherwise → do that

age = 20

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")

#this some topic used in javascript too

#───── IF / ELIF / ELSE CONDITIONS ──────────────────
# Used everywhere in programming!
# Login systems, games, apps, websites
# Literally every program uses conditions!
# Used when you have MORE than 2 options


time = 8

if time >= 8:
    print("You are running behind!")
elif time == 6:
    print("You are early bird!")
else:
    print("You are late>_<")


iq_level = 90

if iq_level == 90:
    print("You are a dolphin")
elif iq_level <=80:
    print("You are good! work on it.")
else:
    print("You are genius")

marks = 75

if marks >= 90:
    print("Grade: A")       # 90 and above
elif marks >= 75:
    print("Grade: B")       # 75 to 89
elif marks >= 60:
    print("Grade: C")       # 60 to 74
elif marks >= 40:
    print("Grade: D")       # 40 to 59
else:
    print("Grade: F")       # below 40


# ── NESTED IF (if inside if) ──────────────
# Used in login systems, security checks!
# Example: checking username AND password

username = "afroj"
password = "1234"

if username == "afroj":
    if password == "1234":
        print("Login successful! Welcome Afroj!")
    else:
        print("Wrong password!")
else:
    print("Username not found!")

# ── REAL WORLD USES ───────────────────────

# 1. GAME LOGIC
player_health = 30

if player_health <= 0:
    print("Game Over!")
elif player_health <= 30:
    print("Warning! Low health!")    # ← this runs
elif player_health <= 60:
    print("Health is okay")
else:
    print("Full health!")

# 2. SHOPPING CART
cart_total = 1500
has_coupon = True

if cart_total >= 1000 and has_coupon:
    discount = cart_total * 0.10    # 10% discount
    print(f"Discount applied! You save ₹{discount}")
    print(f"Final total: ₹{cart_total - discount}")
else:
    print(f"Total: ₹{cart_total}")

# 3. TRAFFIC LIGHT (used in robotics/IoT!)
signal = "green"

if signal == "red":
    print("STOP!")
elif signal == "yellow":
    print("SLOW DOWN!")
elif signal == "green":
    print("GO!")             # ← this runs
else:
    print("Invalid signal!")

# 4. ATM MACHINE LOGIC
balance = 5000
withdraw = 2000

if withdraw > balance:
    print("Insufficient balance!")
elif withdraw <= 0:
    print("Invalid amount!")
else:
    balance -= withdraw      # assignment operator!
    print(f"Withdrawn: ₹{withdraw}")
    print(f"Remaining balance: ₹{balance}")