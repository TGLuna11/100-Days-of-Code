# This is the final project for day 3: Treasure Island
# This project is a text-based adventure game that asks the user to make choices
# to find the treasure and win the game.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Where do you want to go?\n  Type 'left' or 'right': ").lower()
if choice1 == 'left':
    choice2 = input("You come to a lake do you wait for a boat or swim across?\n Type 'wait' or 'swim': ").lower()
    if choice2 == "wait":
        choice3 = input(
            "After waiting for a boat someone takes you to an island with three coloured doors. Red, blue, and yellow. "
            "Which door do you choose?\n Type 'red', 'blue' or 'yellow': ").lower()
        if choice3 == "red":
            print("It's a room full of fire. You got burned by fire. GAME OVER!!!")
        elif choice3 == "blue":
            print("It's a room full of beast. You got eaten by them. GAME OVER!!!")
        elif choice3 == "yellow":
            print("You found the treasure. YOU WIN!!!")
        else:
            print("GAME OVER!!!")
    else:
        print("You got attacked by an angry trout. GAME OVER!!!")

else:
    print("You fell in a hole. GAME OVER!!!")
