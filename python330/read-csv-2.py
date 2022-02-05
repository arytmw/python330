import csv

with open('data.csv','r') as myfile:
    csvfile = csv.DictReader(myfile)

    for lines in csvfile:
        print(lines)
