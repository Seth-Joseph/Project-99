import os, time

path = r"Enter file path here"                #<--- enter file path here
now = time.time()

for filename in os.listdir(path):
    if os.path.getmtime(os.path.join(path, filename)) < now - 30 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))
            print("File Deleted:",filename)
