# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# print all candies in [i] candy format

#for x in candyList:
#print ("[" + str(candyList.index(x)) + "]" + x)

# another way
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])



#ask users five times
for candy in range(allowance):
    candy = input("Which candy would you liek to bring home?")
    candyCart.append(candyList[int(candy)])
    print(candyCart)

#Answer: I brought home with me ....
print("I brought home with me...")
for candy in candyCart:
    print (candy)
