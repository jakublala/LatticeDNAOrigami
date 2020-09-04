#!/bin/sh

# Name of job
#SBATCH -J test_const

# Walltime limit (hours:mins:secs)
#SBATCH -t 5:00:00

# Nodes and procs
#SBATCH -N 1
#SBATCH -n 1

# Standard error and out files
#SBATCH -o outs/test_const.o
#SBATCH -e outs/test_const.e

module unload gcc
module load gcc/6.2.0

echo "Starting job $SLURM_JOB_ID"

export LD_LIBRARY_PATH=~/lib:$LD_LIBRARY_PATH
export PATH=~/bin/$PATH
mkdir -p outs

# Main job
latticeDNAOrigami -i test_const.inp > outs/test_const.out

# Copy results to slowscratch mirror
targetdir=$(pwd | sed "s:home:sharedscratch:")/outs/
mkdir -p $targetdir
cp outs/test_const.* $targetdir/

echo
echo "Job finished. SLURM details are:"
echo
qstat -f ${SLURM_JOB_ID}
echo
echo Finished at `date`
