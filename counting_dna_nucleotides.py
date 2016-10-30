#!/usr/bin/env python3.5
import sys

dna = sys.argv[1]
solution = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

for symbol in dna:
    solution[symbol] += 1

print(" ".join([str(solution['A']),
      str(solution['C']),
      str(solution['G']),
      str(solution['T']),]))
