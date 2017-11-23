# My Info

profile = {"name": "George", 
           "age": 30, 
           "hobbies": ["snowboarding", "surfing", "skateboarding"], 
           "wakeuptime": {"Mon": 5, "Fri": 8, "Sat": 9}
          }

print(profile["name"] + " is " + str(profile["age"]) )
print"On the weekend he gets up at " +str(profile["wakeuptime"]["Sat"])
