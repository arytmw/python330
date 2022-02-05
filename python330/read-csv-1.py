import csv

with open('data.csv','r') as myfile:
    csvfile = csv.reader(myfile)

    for lines in csvfile:
        print(lines)
