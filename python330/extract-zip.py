from zipfile import ZipFile

filename = input("Enter Zip file to extract: ")
dest = input("Enter destination of extraction: ")

with ZipFile(filename,'r') as myzip:
    myzip.extractall(dest)
