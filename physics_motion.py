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