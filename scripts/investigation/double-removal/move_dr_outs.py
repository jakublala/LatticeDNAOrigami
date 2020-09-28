"Retrieve the output folder files from all the simulation setups"
"Place all of the simulation setup folders into a 'sim_outs/' folder"

import os
from shutil import copytree

# Make directory for outputs
if not os.path.exists('outputs'):
    os.makedirs('outputs')
    
# Find all simulation setup directories
dirs = os.listdir('sim_outs/')

# Find and copy the outs folder
for d in dirs:
    tempDirs = os.listdir('sim_outs/{}'.format(d))
    for i in tempDirs:
        if i.find('outs') != -1:
            copytree('sim_outs/{}/{}'.format(d, i), 'outputs/{}'.format(i))
            break
        else:
            continue
            
    

