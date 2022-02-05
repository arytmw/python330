import datetime
from zipfile import ZipFile

filename = input("Enter zip file to read: ")

with ZipFile(filename,'r') as myfile:
    for info in myfile.infolist():
        print(info.filename)
        print(f'\tModified Time: {datetime.datetime(*info.date_time)}')
        print(f'\tCompressed Size: {info.compress_size} Bytes')
        print(f'\tUncompressed Size: {info.file_size} Bytes')
