"Moves all the necessary input files into folders"

import os
from shutil import copy

filebase = 'dr_const'
stapleFile = 'snodin_staples'
jsonFile = 'snodin_unbound'

def read_seqfile(filename):
    """Read seq files in ??? format and strip metadata."""
    with open(filename) as inp:
        seqs = inp.read().split('\n')
        seqs = [seq for seq in seqs if not '>' in seq]
        seqs = [seq for seq in seqs if seq != '']

    return seqs # a list of string sequences


# Names of common input files
biasFunctions = 'bias_functions.json'
movetypes = 'movetypes_default.json'
ops = 'ops_default.json'
archive = 'num_walks.arch'

# Make directory for outputs
if not os.path.exists('sim_folders'):
    os.makedirs('sim_folders')

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

# Iterate through simulation setups
for i in simIndices:
    string = '{}_{}'.format(i[0], i[1])
    # Make simulation output directory for specific simulation setup
    if not os.path.exists('sim_folders/{}/outs_{}'.format(string, string)):
        os.makedirs('sim_folders/{}/outs_{}'.format(string, string))
    
    # Create an empty out file
    with open('sim_folders/{}/outs_{}/{}_{}.out'.format(string, string, filebase, string), 'w'):
        pass
        
    # Copy the files into the specific folders
    copy('configs/{}_{}.inp'.format(filebase, string), 'sim_folders/{}'.format(string))
    copy('jsons/{}_{}.json'.format(jsonFile, string), 'sim_folders/{}'.format(string))
    copy('slurms/{}_{}.sh'.format(filebase, string), 'sim_folders/{}'.format(string))
    
# Copy the files that are the same for all simulation setups
copy('inps/{}'.format(biasFunctions), 'sim_folders/{}'.format(biasFunctions))
copy('inps/{}'.format(movetypes), 'sim_folders/{}'.format(movetypes))
copy('inps/{}'.format(ops), 'sim_folders/{}'.format(ops))
copy('inps/{}'.format(archive), 'sim_folders/{}'.format(archive))
