import sys

for idx, arg in enumerate(sys.argv):
    for key, value in arguments.items():
        if((arg == "--" + key) or (arg == "-" + key[0:1])):
            arguments[key] = coerce(sys.argv[idx+1])
