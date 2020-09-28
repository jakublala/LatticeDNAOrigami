# -*- coding: utf-8 -*-

"Plots the system energy all simulation setups into a single plot"

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
    filename = 'outputs/outs_{}/{}_{}.ene'.format(i, filebase, i)
    data = pd.read_csv(filename, delim_whitespace=True)
    
    # Header read
    if i == 0:        
        # Initialize lists for data accumulation
        means = []
        stds = []

    data = data.rename_axis('ID').values # pandas to a numpy array
    print(data)
    # Data analysis
    dataPoints = data[skippedLogs:, 1] # skip initial non-equilibrium energy values
    mean = dataPoints.mean()
    std = dataPoints.std()

    # Data accumulation
    means.append(mean)
    stds.append(std)


# Plotting
colours = ('b', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'g', 'purple', 'y', 'b')
plt.bar(indices[1:], means[1:], width=0.5, color = colours)
plt.plot([0, 13], [means[0], means[0]], 'r--', label='all staples')
plt.errorbar(indices[1:], means[1:], yerr = stds[1:], fmt='o', markersize = 1, color = 'black')
plt.legend(loc='best')
plt.title('System Energy for Various Staple Types Missing (330 K)')
plt.xlabel('Staple Type Removed')
plt.ylabel('System Energy')
plt.xticks(indices[1:])
plt.xlim(0, 13)
plt.ylim(-530, -450)
plt.show()
