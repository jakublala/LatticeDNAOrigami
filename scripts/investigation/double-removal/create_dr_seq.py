# -*- coding: utf-8 -*-

"Creates seq staple files for all possible combinations when one staple type is missing"

import os

stapleFile = 'snodin_staples'
STAPLE_SEQFILE = 'inps/{}.seq'.format(stapleFile)
CYCLIC = False

COMPLEMENTARY_BASE_PAIRS = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def read_seqfile(filename):
    """Read seq files in ??? format and strip metadata."""
    with open(filename) as inp:
        seqs = inp.read().split('\n')
        seqs = [seq for seq in seqs if not '>' in seq]
        seqs = [seq for seq in seqs if seq != '']

    return seqs # a list of string sequences

def write_seqfile(filename, staple1, staple2):
    with open(filename, "w") as inp:
        for i in range(numberOfStaples): # skip the removed staples
            if i == (staple1 - 1) or i == (staple2 - 1):
                continue
            else:
                inp.write(staples[i])
                inp.write("\n")
            
    return        
        
staples = read_seqfile(STAPLE_SEQFILE) # retrieve staples
numberOfStaples = len(staples) # find number of staples

# Create all simulation combinations
simIndices = []
for i in range(numberOfStaples):
    for j in range(numberOfStaples):
        if i >= j:
            continue
        else:
            simIndices.append([i+1, j+1])

# Make directory for outputs
if not os.path.exists('seqs'):
    os.makedirs('seqs')

# No staple removed simulation setup
OUTPUT_FILENAME = 'seqs/{}_0_0.seq'.format(stapleFile)
write_seqfile(OUTPUT_FILENAME, -1, -1) # no staple removed as no staple with -1 index
    

# Iterate through all remaining simulation setups
for removedStaples in simIndices:
    OUTPUT_FILENAME = 'seqs/{}_{}_{}.seq'.format(stapleFile, removedStaples[0], removedStaples[1])
    write_seqfile(OUTPUT_FILENAME, removedStaples[0], removedStaples[1])
      