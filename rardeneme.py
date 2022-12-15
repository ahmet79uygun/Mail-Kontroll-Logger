import os
import shutil

if os.path.exists("sends"):
    shutil.rmtree("sends")

import os, shutil

fpath = 'C:/Users/uygun/PycharmProjects/mfinish/'
path = os.getcwd()

for file in os.listdir(path):
    if file.endswith("sends.zip"):
        dirs = os.path.join(path, file)

if os.path.exists(fpath):
    shutil.rmtree(fpath)
    os.mkdir(fpath)

os.remove(dirs)
