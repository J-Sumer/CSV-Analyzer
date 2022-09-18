import sys
from helperFunctions import *

the = {
    "eg": "nothing",
    "dump": False,
    "file": "test.csv",
    "help": False,
    "nums": 512,
    "seed": 10019,
    "Seperator": ","
}

def updateCli(the):
    for idx, arg in enumerate(sys.argv):
        for key, value in the.items():
            if((arg == "--" + key) or (arg == "-" + key[0:1])):
                the[key] = coerce(sys.argv[idx+1])

def getArguments():
    return the