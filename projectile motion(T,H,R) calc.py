import math 

# Constant for gravity = g (m/s^2)
g = 9.81

print("--- Detailed Projectile Motion Calculator ---")

while True:
    try:
        user_input = input("\nEnter initial velocity in m/s (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
            
        v = float(user_input)
        angle_deg = float(input("Enter launch angle in degrees: "))

        # 1. Convert degrees to radians
        angle_rad = math.radians(angle_deg)

        # 2. Velocity components
        vx = v * math.cos(angle_rad)
        vy = v * math.sin(angle_rad)

        # 3. Core Physics Calculations
        time_of_flight = (2 * vy) / g
        max_height = (vy**2) / (2 * g)
        horizontal_range = vx * time_of_flight

        # 4. Display Summary
        print("-" * 35)
        print(f"Total Flight Time: {round(time_of_flight, 2)} s")
        print(f"Maximum Height:    {round(max_height, 2)} m")
        print(f"Horizontal Range:  {round(horizontal_range, 2)} m")
        print("-" * 35)

        # 5. Bonus: Check height at a specific time
        check_t = input("Check height at a specific time? (Enter seconds or 'n'): ")
        if check_t.lower() != 'n':
            t = float(check_t)
            # Formula: s = (vy * t) - (0.5 * g * t^2)
            current_height = (vy * t) - (0.5 * g * (t**2))
            if t > time_of_flight:
                print(f"At {t}s, the object has already hit the ground!")
            else:
                print(f"Height at {t}s: {round(current_height, 2)} m")

    except ValueError:
        print("Error: Please enter numbers only.")