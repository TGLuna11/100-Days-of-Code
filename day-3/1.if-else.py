print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!!")
    age = int(input("What is your age? "))
    bill = 0
    # Nested if statements
    if age <= 12:
        print("Your ticket price will be £5")
        bill = 5
    elif age <= 18:  # This elif statement is only checked if the previous if statement is False
        print("Your ticket price will be £7")
        bill = 7
    else:  # This else statement is only checked if all previous if and elif statements are False
        print("Your ticket price will be £12")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y for yes or N for no: ").lower()
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is £{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
