#!/bin/sh

# Name of job
#SBATCH -J dr_const_0_0

# Walltime limit (hours:mins:secs)
#SBATCH -t 24:00:00

# Nodes and procs
#SBATCH -N 1
#SBATCH -n 1


# Standard error and out files
#SBATCH -o outs_0_0/dr_const_0_0.o
#SBATCH -e outs_0_0/dr_const_0_0.e

module unload gcc
module load gcc/6.2.0

echo "Starting job $SLURM_JOB_ID"

export LD_LIBRARY_PATH=~/lib:$LD_LIBRARY_PATH
export PATH=~/bin/$PATH
mkdir -p outs_0_0

# Main job
~/LatticeDNAOrigami/bin/latticeDNAOrigami -i dr_const_0_0.inp > outs_0_0/dr_const_0_0.out

echo
echo "Job finished. SLURM details are:"
echo
qstat -f ${SLURM_JOB_ID}
echo
echo Finished at `date`
