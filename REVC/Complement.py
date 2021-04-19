#!/usr/bin/python3

#Reverse complement of DNA string
#Note the directionality of the strands
#   5' --- 3'
#   3' --- 5'

import sys

fname = sys.argv[-1]

f = open(fname, "r")
try:
    instring = f.readline()

    Comp = ""

    for i in range(0, len(instring)):
        if instring[i] == 'A':
            Comp += 'T'
        elif instring[i] == 'T':
            Comp += 'A'
        elif instring[i] == 'C':
            Comp += 'G'
        elif instring[i] == 'G':
            Comp += 'C'

    revComp = Comp[::-1]

finally:
    f.close()

print(revComp)


