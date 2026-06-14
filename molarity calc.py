# Molarity Calculator (mol/L)
print("--- Molarity Calculator ---")

while True:
    try:
        # 1. Get user input
        moles = float(input("\nEnter no. of moles of your solute: "))
        
        # Allow user to type 'exit' to close the program
        if moles == 'exit':
            break
        
        volume_ml = float(input("Enter volume of solution in mL: "))

        # 2. Check for zero or negative volume
        if volume_ml <= 0:
            print("Error: Volume must be greater than zero.")
            continue

        # 3. Calculate Molarity
        # Formula: M = moles / liters
        volume_liters = volume_ml / 1000
        molarity = moles / volume_liters

        # 4. Display result rounded to 4 decimal places
        print(f"Result: The molarity is {round(molarity, 4)} M")
        
    except ValueError:
        print("Error: Please enter valid numbers.")

    print("\n(Type 'exit' to quit or enter new values to calculate again)")