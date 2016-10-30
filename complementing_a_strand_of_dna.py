#!/usr/bin/env python3.5
import sys

dna = sys.argv[1]
dna = dna[::-1]

dna = dna.replace('A', 't')
dna = dna.replace('T', 'a')
dna = dna.replace('C', 'g')
dna = dna.replace('G', 'c')

print(dna.upper())
