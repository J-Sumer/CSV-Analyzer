from cli import *

help = """
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

USAGE: lua seen.lua [OPTIONS]

OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --Seperator feild seperator                       = , 
"""

arguments = {
    "eg": "nothing",
    "dump": False,
    "file": "test.csv",
    "help": False,
    "nums": 512,
    "seed": 10019,
    "Seperator": ","
}

updateCli(arguments)