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