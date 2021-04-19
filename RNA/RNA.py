#!/usr/bin/python3

#Transcribing DNA into RNA

import sys

fname = sys.argv[-1]

f = open(fname, "r")
try:
    instring = f.readline()

    RNA=""

    for i in range(0, len(instring)):
        if instring[i] == 'T':
            RNA += 'U'
        else:
            RNA += instring[i]
finally:
    f.close()
print(RNA)
