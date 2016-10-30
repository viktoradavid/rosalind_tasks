#!/usr/bin/env python3.5
import sys

dna1 = sys.argv[1]
dna2 = sys.argv[2]

differences = 0
for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        differences += 1

print(differences)
