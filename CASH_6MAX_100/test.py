from os import listdir, walk
from os.path import isfile, join
import os

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    print(f'dirpath {dirpath}')
    print(f'dirnames {dirnames}')
    print(f'filenames {filenames}')