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

def write_seqfile(filename, removedStaple):
    with open(filename, "w") as inp:
        for i in range(numberOfStaples): # skip the removed staple
            if i == removedStaple:
                continue
            else:
                inp.write(staples[i])
                inp.write("\n")
            
    return        
        
staples = read_seqfile(STAPLE_SEQFILE) # retrieve staples
numberOfStaples = len(staples) # find number of staples

# Make directory for outputs
if not os.path.exists('seqs'):
    os.makedirs('seqs')

# No staple removed simulation setup
OUTPUT_FILENAME = 'seqs/{}_0.seq'.format(stapleFile)
write_seqfile(OUTPUT_FILENAME, -1) # no staple removed as no staple with -1 index
    

# Iterate through all remaining simulation setups
for stapleIndex in range(numberOfStaples):
    OUTPUT_FILENAME = 'seqs/{}_{}.seq'.format(stapleFile, stapleIndex + 1)
    write_seqfile(OUTPUT_FILENAME, stapleIndex)
        