import hashlib
import os

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as t:
        for chunk in iter(lambda: t.read(4096), b""):
            hash_md5.update(chunk)
    	return hash_md5.hexdigest()

path = os.getenv("home")
def find_file(extension):
    for root, subFolder, files in os.walk(home):
        for item in files:
            if item.endswith("."+ str(extension)):
                fileNamePath = str(os.path.join(root,item))
                print(fileNamePath," ",md5(fileNamePath))


a = input("enter file extension for search operation:")
find_file(a)

