"Moves all the necessary input files into folders"

import os
from shutil import copy

filebase = 'sr_const'

# Names of common input files
biasFunctions = 'bias_functions.json'
movetypes = 'movetypes_default.json'
ops = 'ops_default.json'
archive = 'num_walks.arch'

# Make directory for outputs
if not os.path.exists('sim_folders'):
    os.makedirs('sim_folders')

# Get config files
configFiles = os.listdir('configs')
configFiles.sort(key=lambda s: len(s)) # sort by index (length)

# Get JSON files
jsonFiles = os.listdir('jsons')
jsonFiles.sort(key=lambda s: len(s)) # sort by index (length)

# Get slurm files
slurmFiles = os.listdir('slurms')
slurmFiles.sort(key=lambda s: len(s)) # sort by index (length)

indices = [i for i in range(len(configFiles))] # create indices list

# Iterate through simulation setups
for i in indices:
    # Make simulation output directory for specific simulation setup
    if not os.path.exists('sim_folders/{}/outs_{}'.format(i, i)):
        os.makedirs('sim_folders/{}/outs_{}'.format(i, i))
    
    # Create an empty out file
    with open('sim_folders/{}/outs_{}/{}_{}.out'.format(i, i, filebase, i), 'w'):
        pass
        
    # Copy the files into the specific folders
    copy('configs/{}'.format(configFiles[i]), 'sim_folders/{}'.format(i))
    copy('jsons/{}'.format(jsonFiles[i]), 'sim_folders/{}'.format(i))
    copy('slurms/{}'.format(slurmFiles[i]), 'sim_folders/{}'.format(i))

# Copy the files that are the same for all simulation setups
copy('inps/{}'.format(biasFunctions), 'sim_folders/{}'.format(biasFunctions))
copy('inps/{}'.format(movetypes), 'sim_folders/{}'.format(movetypes))
copy('inps/{}'.format(ops), 'sim_folders/{}'.format(ops))
copy('inps/{}'.format(archive), 'sim_folders/{}'.format(archive))
