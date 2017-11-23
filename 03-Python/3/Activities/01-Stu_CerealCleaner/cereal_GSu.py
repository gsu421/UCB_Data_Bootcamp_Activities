# import os
# csvpath = os.path.join('Resources', 'cereal.csv')


# import csv
# with open(csvpath) as csvfile:
#     pass
#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=' ')

#     print(csvreader)

#     #  Each row is read as a row
#     for row in csvreader:
#         print(row)

import os
import csv
csvpath = os.path.join('Resources','cereal.csv')

#Open and read csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.read(csvfile, delimiter=",")

    #Iterate through ach row
    for row in csvreader:
        if float(row[7]) >=5:
            print(row)



