# -*- coding: utf-8 -*-

"Plots the system energy all simulation setups into a single plot"

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

filebase = 'dr_const'
stapleFile = 'snodin_staples'
skippedLogs = 300

def read_seqfile(filename):
    """Read seq files in ??? format and strip metadata."""
    with open(filename) as inp:
        seqs = inp.read().split('\n')
        seqs = [seq for seq in seqs if not '>' in seq]
        seqs = [seq for seq in seqs if seq != '']

    return seqs # a list of string sequences

numberOfStaples = len(read_seqfile('inps/{}.seq'.format(stapleFile)))

# Create all simulation combinations
simIndices = []
for i in range(numberOfStaples):
    for j in range(numberOfStaples):
        if i >= j:
            continue
        else:
            simIndices.append([i+1, j+1])
simIndices.insert(0, [0, 0]) # no staples removed setup

# Make indices into strings
simStrings = []
for i in simIndices:
    simStrings.append('{}_{}'.format(i[0], i[1]))

# Initialize lists for data accumulation
means = []
stds = []

# Iterate through simulation setups
for i in simStrings:
    # Retrive the order parameter data
    filename = 'outputs/outs_{}/{}_{}.ene'.format(i, filebase, i)
    data = pd.read_csv(filename, delim_whitespace=True)
    data = data.rename_axis('ID').values # pandas to a numpy array
    
    # Data analysis
    dataPoints = data[skippedLogs:, 1] # skip initial non-equilibrium energy values
    mean = dataPoints.mean()
    std = dataPoints.std()

    # Data accumulation
    means.append(mean)
    stds.append(std)



# Plotting
#colours = ('b', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'b')
# Create labels
xlabels = np.arange(len(simIndices[1:]))
xTicks = []
for i in simIndices:
    xTicks.append('{}_{}'.format(i[0], i[1]))

plt.figure(num=None, figsize=(25, 12), dpi=150, facecolor='w', edgecolor='k')
plt.bar(xlabels, means[1:], width=0.5)
plt.plot([-1, 66], [means[0], means[0]], 'r--', label='all staples')
plt.errorbar(xlabels, means[1:], yerr = stds[1:], fmt='o', markersize = 1, color = 'black')
plt.legend(loc='best')
plt.title('System Energy for Various Two Staple Types Missing (330 K)')
plt.xlabel('Staple Types Removed')
plt.ylabel('System Energy')
plt.xticks(range(len(simIndices)), xTicks[1:])
plt.xlim(-1, 66)
plt.rcParams.update({'font.size': 8})
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
plt.ylim(-530, -350)
plt.show()
