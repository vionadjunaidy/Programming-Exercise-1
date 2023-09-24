print("Enter your height")
Feet = int(input("Feet: "))
Inches = int(input("Inches: "))
feet_in_cm = Feet * 30.48
inches_in_cm = Inches * 2.54
feet_and_inches_incm = feet_in_cm + inches_in_cm
board = feet_and_inches_incm * 88/100
print(f'Suggested board lenght = {board} cm')