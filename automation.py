import os
import shutil

source = input()
destination = input()
ext = input()

for file in os.listdir(source):
    if file.endswith(ext):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))
