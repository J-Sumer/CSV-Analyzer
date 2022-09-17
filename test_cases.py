from helperFunction import *
from cli import *
from Num import *
from Sym import *
from Data import *

updateCli()
eg = {}
args = getArguments()

def runs(test):
    out = False
    if test in eg:
        if(args["dump"]):
            out = eg[test]()
        else:
            try:
                out = eg[test]()
                if(out):
                    print("!!!!!! ", "PASS   ", test, "    true")
                else:
                    print("!!!!!! ", "PASS   ", test, "    false")
            except:
                print("!!!!!! ", "CRASH   ", test, "    false")

def ALL():
    for test in eg:
        if(test != "ALL"):
            print("\n-----------------------------------")
            runs(test)