def greet():
    print("_______________________")
    print("\nWelcome to ANQ ships, Your one-stop shop for Rocketships")
    print("_______________________\n")
    print("-----------------------")
    print("Available Rocketships")
greet()
def line():
    print("-----------------------")
# Lists of rocketship and also the rates.
print("""(1) Rocket Lab Photon $10000
(2) SpaceX Falcon 9 $5000
(3) Blue Origin New Shepard $8000
(4) Exit
----------""")

# Storing rockets and their costs.
rocketcount = []

# I have created a loop to manage the hiring process.
while True:
    # Check if all rockets are chosen.
    if len(rocketcount) == 3:
        print("\nNo more rockets are available.")
        break  # If all rockets are unavailable, break the code.

    # Rocket hiring process.
    choice = input("\nEnter your choice (1, 2, 3 or 4): ")
    if choice == "1" and "Rocket Lab Photon" not in [rocket[0] for rocket in rocketcount]:
        rocket, costperday = "Rocket Lab Photon", 10000
    elif choice == "2" and "SpaceX Falcon 9" not in [rocket[0] for rocket in rocketcount]:
        rocket, costperday = "SpaceX Falcon 9", 5000
    elif choice == "3" and "Blue Origin New Shepard" not in [rocket[0] for rocket in rocketcount]:
        rocket, costperday = "Blue Origin New Shepard", 8000
    elif choice == '4':
        print("Have a good day. Goodbye!")
        break
    else:
        print("\n***This rocket has already been hired or the choice is invalid. Try again.***")
        continue  # if input is invalid then go back to the top.
    
    rocketcount.append((rocket, costperday))
    print(f"\nYou selected {rocket}")

    # Hire period, pilot, and passengers for the selected rocket.
    hire_days = int(input("\nEnter hire period for this rocket (1-30 days): "))
    while not (1 <= hire_days <= 30):
        hire_days = int(input("\n***Invalid number of days. Enter between 1 and 30.***"))

    while True:
        pilot = input("\nDo you need a pilot (y/n): ").lower()
        if pilot == "y":
            print("\nWe will provide you with a pilot.")
            break
        elif pilot == "n":
            print("\nNo pilot will be provided.")
            break
        else:
            print("\n***Invalid input, choose yes or no***")

    while True:
        try:
            no_ppl = int(input("\nEnter number of passengers (1-10): "))
            if 1 <= no_ppl <= 10:
                break
            else:
                print("\n***Invalid number of passengers. Enter between 1 and 10.***")
        except ValueError:
            print("\n***Invalid input. Please enter a number between 1 and 10.***")

    # Include the hire period in the hired rocket details.
    rocketcount[-1] = (rocketcount[-1][0], rocketcount[-1][1], hire_days)

    # Ask if the user wants to hire more rockets.
    more_rockets = input("\nWould you like to hire another rocket? (y/n): ").lower()
    if more_rockets == "n":
        break  # If the answer is No then end the code.
    elif more_rockets != "y":
        print("\n***Invalid input. Please choose 'y' or 'n'.***")

# Calculate the total cost.
total_cost = 0
for rocket in rocketcount:
    rocket_name, rocket_cost, rocket_days = rocket
    total_cost += rocket_cost * rocket_days  # default cost per rocket per hire period

    if pilot == "yes":
        total_cost += 500 * rocket_days  # Add $500 per day for the pilot.

    total_cost += 500 * no_ppl  # Add $500 per passenger per day.

# Print the receipt.
print("\n--- Receipt ---")
for rocket in rocketcount:
    rocket_name, rocket_cost, rocket_days = rocket
    print("Spacecraft:", rocket_name)
    print("Cost per Day: $", rocket_cost)
    print("Hire Period:", rocket_days, "days")
    print("_______________________")

print(f"\nTotal Cost: ${total_cost}")
