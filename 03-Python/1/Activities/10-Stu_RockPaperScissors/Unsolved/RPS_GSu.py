
# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
    # r wins s
if (user_choice == "r" and computer_choice == "r"):
    print("You choo=se rock. The computer chose paper.")
    print("it's a tie")
elif (user_choice == "r" and computer_choice == "p"):
    print("you loose")
elif (user_choice == "r" and computer_choice == "s"):
    print("congratulations! you WIN!!!")
    
    # s wins p
elif (user_choice == "s" and computer_choice == "s"):
    print("it's a tie")
elif (user_choice == "s" and computer_choice == "r"):
    print("you loose")
elif (user_choice == "s" and computer_choice == "p"):
    print("congratulations! you WIN!!!")
                    
    # p wins r
elif (user_choice == "p" and computer_choice == "p"):
    print("it's a tie")
elif (user_choice == "p" and computer_choice == "s"):
    print("you loose")
elif (user_choice == "p" and computer_choice == "r"):
    print("congratulations! you WIN!!!")
