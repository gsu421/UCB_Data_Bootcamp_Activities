import os
import csv

video = input("What show or movie are you looking for?")

#Set Path for the file
csvpath = os.path.join('Resources','netflix_ratings.csv')

found = False

#Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")




#Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + "is rated " + row[1] + " with a rating of " + row[6])

            found = True
    if found == False:
        print("sorry, bro")




