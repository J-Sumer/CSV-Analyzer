import sys

def updateCli(arguments):
    for idx, arg in enumerate(sys.argv):
        for key, value in arguments.items():
            if((arg == "--" + key) or (arg == "-" + key[0:1])):
                arguments[key] = coerce(sys.argv[idx+1])

def coerce(str):
    if(str.lower() == "true"):
        return True
    if(str.lower() == "false"):
        return False
    try:
        return int(str)
    except:
        pass
    return str.strip()
