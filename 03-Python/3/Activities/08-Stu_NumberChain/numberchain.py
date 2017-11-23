answer = "y"

# while answer == "y":
#     number = input("how many number?")
#     for x in range (0,int(number)+1):
#         print(x)

#     answer = input("Would you like to continue? (y)es or (n)o.")

#Bonus
initial = 0
while answer == "y":
    number = input("how many number?")
    for x in range (initial,int(number)+1):
        initial = x
        print(x)

    answer = input("Would you like to continue? (y)es or (n)o.")


