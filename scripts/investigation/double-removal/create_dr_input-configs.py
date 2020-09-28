# -*- coding: utf-8 -*-

"Creates input configuration files for DR simulation"

import os

filebase = 'dr_const'
stapleFile = 'snodin_staples'
jsonFile = 'snodin_unbound'
template = 'inps/input_template.inp'

def read_seqfile(filename):
    """Read seq files in ??? format and strip metadata."""
    with open(filename) as inp:
        seqs = inp.read().split('\n')
        seqs = [seq for seq in seqs if not '>' in seq]
        seqs = [seq for seq in seqs if seq != '']

    return seqs # a list of string sequences

def change_param(tempParams, parameter, append):
    """Changes the parameter from the input configuration template"""
    index = [k for k, s in enumerate(tempParams) if parameter in s][0]
    tempParams[index] = '{}={}'.format(parameter, append)
    return tempParams

with open(template, 'r') as file:
    params = file.readlines()

# Make directory for outputs
if not os.path.exists('configs'):
    os.makedirs('configs')

numberOfStaples = len(read_seqfile('inps/{}.seq'.format(stapleFile)))

# Create all simulation combinations
simIndices = []
for i in range(numberOfStaples):
    for j in range(numberOfStaples):
        if i >= j:
            continue
        else:
            simIndices.append([i+1, j+1])

# No staple simulation setup
simIndices.append([0, 0])


for i in simIndices: # iterate through all simulation setups
    tempParams = params[:] # copy parameters without reference  
    
    # Manually change the parameters that are different
    # Input JSON Filename
    keyword = 'origami_input_filename'
    newParam = '{}_{}_{}.json\n'.format(jsonFile, i[0], i[1])
    tempParams = change_param(tempParams, keyword, newParam)
    
    # Output Directory
    keyword = 'output_filebase'
    newParam = 'outs_{}_{}/{}_{}_{}\n'.format(i[0], i[1],filebase, i[0], i[1])
    tempParams = change_param(tempParams, keyword, newParam)    
    
    # Create the input configuration file
    output = 'configs/{}_{}_{}.inp'.format(filebase, i[0], i[1])
    with open(output, 'w') as file:
        file.writelines(tempParams)
        
