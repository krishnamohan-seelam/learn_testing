import os 

def rm(file):
    os.remove(file)

def rm2(file):
    if os.path.isfile(file):
        os.remove(file)