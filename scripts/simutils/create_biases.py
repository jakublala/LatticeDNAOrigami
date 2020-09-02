#!/usr/bin/env python3

"""Create bias input file"""

import numpy as np
import json


OUTPUT_FILENAME = 'simulation/bias_functions.json'

bias_functions = [] # initializes the list of bias functions
single_biasFunction = {'type':{}, 'label':{}, 'tag':{}, 'level':{}, 'ops':{}, 'bias_funcs':{}}
numberOfBiasFunctions = 1
types = ['LinearStep', 'LinearStepWell', 'SquareWell', 'Grid']

for i in range(numberOfBiasFunctions):
    b = single_biasFunction.copy()
    b['type'] = types[0]
    b['label'] = 
    b['tag'] = 
    b['level'] = 
    b['ops'] =
    b['bias_funcs'] = 
    bias_functions.append(single_biasFunction)

# Output JSON file
json_bias_func = {'origami':{}}
json_bias_func['origami']['bias_functions'] = bias_functions
json.dump(json_bias_func, open(OUTPUT_FILENAME, 'w'), indent=4, separators=(',', ': '))

