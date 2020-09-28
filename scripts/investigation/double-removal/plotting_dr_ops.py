# -*- coding: utf-8 -*-

"Plots the order parameters of all simulation setups into a single plot"

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

filebase = 'dr_const'
skippedLogs = 300
stapleFile = 'snodin_staples'

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

# Iterate through simulation setups
for i in simIndices:
    # Retrive the order parameter data
    filename = 'outputs/outs_{}_{}/{}_{}_{}.ops'.format(i[0], i[1], filebase, i[0], i[1])
    data = pd.read_csv(filename, delim_whitespace=True)
    
    # Header read
    if i == [0, 0   ]:        
        # Initialize lists for data accumulation
        ops = {}
        opsTags = []
        means = []
        stds = []

        for k in range(len(data.columns)):
            opTag = data.columns[k] # retrieve order parameter tag
            opTag = opTag[:-1] # remove extra comma separator
        
            # Find the label of the order parameter tag
            with open('inps/ops_default.json') as f:
                jsonFile = json.load(f)
                for j in jsonFile['origami']['order_params']:
                    if opTag == j['tag']:
                        opLabel = j['label']
                    else:
                        continue
            ops[opTag] = opLabel
            opsTags.append(opTag)
            means.append([])
            stds.append([])


    data = data.rename_axis('ID').values # pandas to a numpy array

    # Data analysis
    for k in enumerate(ops):
        dataPoints = data[skippedLogs:, k[0]] # skips initial non-equilibrium ops values
        mean = dataPoints.mean()
        std = dataPoints.std()
    
        # Data accumulation
        means[k[0]].append(mean)
        stds[k[0]].append(std)
    
# Create labels
xlabels = np.arange(len(simIndices[1:]))
xTicks = []
for i in simIndices:
    xTicks.append('{}_{}'.format(i[0], i[1]))

# Plotting
for plotMeans in enumerate(means):
    plotData = plotMeans[1]
    errorData = stds[plotMeans[0]]
    #colours = ('b', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'b')
    plt.figure(num=None, figsize=(25, 12), dpi=150, facecolor='w', edgecolor='k')
    plt.bar(xlabels, plotData[1:], width=0.5)
    plt.plot([-1, 66], [plotData[0], plotData[0]], 'r--', label='all staples')
    plt.errorbar(xlabels, plotData[1:], yerr = errorData[1:], fmt='o', markersize = 1, color = 'black')
    plt.legend(loc='best')
    plt.title('Order Parameter for Various Staple Types Missing (330 K)')
    plt.xlabel('Staple Type Removed')
    plt.ylabel('{}'.format(ops[opsTags[plotMeans[0]]]))
    plt.xticks(range(len(xlabels)), xTicks[1:])
    plt.xlim(-1, 66)
    plt.rcParams.update({'font.size': 8})
    plt.show()
