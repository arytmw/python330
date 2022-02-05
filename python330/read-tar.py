import tarfile

filename = input("Path to the TAR file to read: ")

tar_content = tarfile.open(filename)

for data in tar_content.getnames():
    print(data)
