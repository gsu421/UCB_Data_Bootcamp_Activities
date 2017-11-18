
from collections import Counter
pie = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee', 'Black Bun', 'Blueberry', 'Buko', 'Burek', 'Tamale', 'Steak']

#list to store user's purcahse
list = []
print("Welcome to the House of Pies! here are our pies:")

answer = "y"
while (answer == "y"):
    for i in range(len(pie)):
        print("[" + str(i+1) + "]" + pie[i])
    select = input("Which would you like?")
    list.append(pie[int(int(select)-1)])

    #print(list)
    answer = input("Great! Another purchase? (y)es or (n)o")

print("you purchase a total of" + str(len(list)))

#for i in range(len(list)):
print("you purchased" + str(list.count(i)) + list[i])
#print(Counter(list))

