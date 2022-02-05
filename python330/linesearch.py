import re

filename = input("Enter filename to search in: ")
regexp = input("Enter word to search: ")
linenum = 0

with open(filename) as f:
    for line in f:
        linenum = linenum + 1
        result = re.findall(regexp,line)
        if result:
            print(f"{linenum} {result}")
