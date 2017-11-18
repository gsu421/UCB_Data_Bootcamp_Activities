
#X = 1
#y = 10

x = int(input("What's the value for x?"))
y = int(input("What is the value for y?"))
#Checks if one value is equal to another
if (x ==1):
    print ("x is qual to 1")

if y != 1:
    print("y is not equal to 1")

if (x<y):
    print("x is less than y")

if (x>=1):
    print("x is greater than or equal to 1")

if (x == 1 and y ==10):
    print("Both values returned true")

if (x<45 or y <5):
    print("One or the other statements were true")

#Nested if statements
if(x<10):
    if(y<5):
        print("x is less than 10 and y is less than 5")
    elif(y==5):
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")



