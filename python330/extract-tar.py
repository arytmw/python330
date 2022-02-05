import tarfile

filename = input("Enter TAR file to extract: ")
dest_name = input("Enter extract destination: ")

tar_file = tarfile.open(filename)
tar_file.extractall(dest_name)
