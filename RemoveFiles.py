import os;
import shutil;
import time;

path = input("Enter path of the file to delete :")
now = time.time()
f = os.path.join(path,f)
for f in os.listdir(path) :
    if os.stat(f).st_mtime < now - 7 *86400 :
        if os.path.isfile(f):
            os.remove(os.path.join(path,f))