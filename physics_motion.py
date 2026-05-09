import sys
sys.stdout.reconfigure(encoding='utf-8')

# ── PHYSICS MOTION IN PYTHON ──────────────
# Position, Speed, Velocity using Python!

# ── 1. POSITION ───────────────────────────
starting_position = 0
current_position = 50    # 50 meters from start

print(f"Starting position: {starting_position}m")
print(f"Current position: {current_position}m")

# ── 2. DISTANCE AND DISPLACEMENT ──────────
# Belly walks 4m east then 4m west

start = 0
end = 0              # back to starting point

# distance = total path travelled
distance = 4 + 4     # 8 meters total
print(f"Distance travelled: {distance}m")

# displacement = end - start
displacement = end - start
print(f"Displacement: {displacement}m")

# ── 3. SPEED ──────────────────────────────
# Speed = distance / time

def calculate_speed(distance, time):
    if time == 0:
        return 0      # can't divide by zero!
    return distance / time

# train example
train_distance = 300    # km
train_time = 3          # hours
train_speed = calculate_speed(train_distance, train_time)
print(f"Train speed: {train_speed} km/h")

# ── 4. VELOCITY ───────────────────────────
# Velocity = displacement / time

def calculate_velocity(displacement, time):
    if time == 0:
        return 0
    return displacement / time

# Belly walking example
belly_displacement = 0   # back to start
belly_time = 8           # seconds
belly_velocity = calculate_velocity(belly_displacement, belly_time)
print(f"Belly velocity: {belly_velocity} m/s")

# ── 5. INTERACTIVE CALCULATOR ─────────────
# Let user calculate speed and velocity!

print("\n── MOTION CALCULATOR ──")
print("1. Speed Calculator")
print("2. Velocity Calculator")
print("3. Both")

choice = input("Choose (1/2/3): ")

if choice == "1":
    d = float(input("Enter distance (m): "))
    t = float(input("Enter time (s): "))
    speed = calculate_speed(d, t)
    print(f"Speed = {speed} m/s")
   
elif choice == "2":
    disp = float(input("Enter displacement (m): "))
    t = float(input("Enter time (s): "))
    velocity = calculate_velocity(disp, t)
    print(f"Velocity = {velocity} m/s")

elif choice == "3":
    d = float(input("Enter total distance (m): "))
    disp = float(input("Enter displacement (m): "))
    t = float(input("Enter time (s): "))
    speed = calculate_speed(d, t)
    velocity = calculate_velocity(disp, t)
    print(f"Speed = {speed} m/s")
    print(f"Velocity = {velocity} m/s")
    if speed == abs(velocity):
        print("Speed equals velocity magnitude!")
        print("Straight line motion!")
    else:
         print("Invalid choice!")

# ── 6. POSITION TRACKER ───────────────────
# Track someone moving step by step!

print("\n── POSITION TRACKER ──")
position = 0
total_distance = 0
steps = int(input("How many moves? "))

for i in range(steps):
    move = float(input(f"Move {i+1} (+ east, - west): "))
    position += move
    total_distance += abs(move)   # abs = always positive!
    print(f"Current position: {position}m")
    print(f"Total distance so far: {total_distance}m")

print(f"\nFinal position: {position}m")
print(f"Total distance: {total_distance}m")
print(f"Displacement: {position}m")
print(f"Are they same? {position == total_distance}")