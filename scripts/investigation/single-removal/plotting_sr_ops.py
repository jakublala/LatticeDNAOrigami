# -*- coding: utf-8 -*-

"Plots the order parameters of all simulation setups into a single plot"

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

filebase = 'sr_const'
skippedLogs = 300

# Get list of all output folders of different simulation setups
simFolders = os.listdir('outputs')
simFolders.sort(key=lambda s: len(s))

indices = [i for i in range(len(simFolders))] # create indices list

# Iterate through simulation setups
for i in indices:
    # Retrive the order parameter data
    filename = 'outputs/outs_{}/{}_{}.ops'.format(i, filebase, i)
    data = pd.read_csv(filename, delim_whitespace=True)
    
    # Header read
    if i == 0:        
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
    

# Plotting
for plotMeans in enumerate(means):
    plotData = plotMeans[1]
    errorData = stds[plotMeans[0]]
    colours = ('b', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'b')
    plt.bar(indices[1:], plotData[1:], width=0.5, color = colours)
    plt.plot([0, 13], [plotData[0], plotData[0]], 'r--', label='all staples')
    plt.errorbar(indices[1:], plotData[1:], yerr = errorData[1:], fmt='o', markersize = 1, color = 'black')
    plt.legend(loc='best')
    plt.title('Order Parameter for Various Staple Types Missing (330 K)')
    plt.xlabel('Staple Type Removed')
    plt.ylabel('{}'.format(ops[opsTags[plotMeans[0]]]))
    plt.xticks(indices[1:])
    plt.xlim(0, 13)
    plt.show()
