#!/usr/bin/env python3.5
import sys


gc_contents = []
with open('gc_content.txt', 'r') as data:
    name = ""
    dna_string = ""
    for line in data.readlines():
        if line.startswith(">"):
            gc_contents.append((name, dna_string))
            name = line[1:].replace('\n', '')
            dna_string = ""
        else:
            dna_string += line.replace('\n', '')

    gc_contents.append((name, dna_string))

gc_contents = gc_contents[1:]

# (dataset_name, gc_content)
max_gc = ("", 0)

for input_data in gc_contents:
    g_count = input_data[1].count('G')
    gc_count = g_count + input_data[1].count('C')

    gc = float(gc_count)/float(len(input_data[1]))
    if gc > max_gc[1]:
        max_gc = (input_data[0], gc)

print(max_gc[0])
print(max_gc[1] * 100)
