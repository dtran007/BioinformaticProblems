#!/usr/bin/python3

#Counting DNA Nucleotides

import sys

fname = sys.argv[-1]

f = open(fname, "r")
try:
    instring = f.readline()

    A=0
    C=0
    G=0
    T=0

    for i in range(0, len(instring)):
        if  instring[i] == 'A':
            A += 1
        elif instring[i] == 'C':
            C += 1
        elif instring[i] == 'G':
            G += 1
        elif instring[i] == 'T':
            T += 1

finally:
    f.close

print("{0} {1} {2} {3}".format(A, C, G, T))


