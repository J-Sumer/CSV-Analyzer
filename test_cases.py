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

def BAD():
    print(eg.this_is_not_there)
    
def LIST():
    print("Examples lua csv -e ...")
    for key in eg:
        print("\t" + key)
    return True

def the():
    printDic(args)
    return True

def sym():
    sym = Sym()
    list = ["a","a","a","a","b","b","c"]
    for x in list:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    printDic({"mid": mode,"div": entropy})
    return True

def num():
    num = Num(0, "num")
    for i in range(1,101):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid , "    ", div)
    return True 

def ALL():
    for test in eg:
        if(test != "ALL"):
            print("\n-----------------------------------")
            runs(test)