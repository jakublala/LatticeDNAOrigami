#!/bin/sh

# Name of job
#SBATCH -J dr_const_1_12

# Walltime limit (hours:mins:secs)
#SBATCH -t 24:00:00

# Nodes and procs
#SBATCH -N 1
#SBATCH -n 1


# Standard error and out files
#SBATCH -o outs_1_12/dr_const_1_12.o
#SBATCH -e outs_1_12/dr_const_1_12.e

module unload gcc
module load gcc/6.2.0

echo "Starting job $SLURM_JOB_ID"

export LD_LIBRARY_PATH=~/lib:$LD_LIBRARY_PATH
export PATH=~/bin/$PATH
mkdir -p outs_1_12

# Main job
~/LatticeDNAOrigami/bin/latticeDNAOrigami -i dr_const_1_12.inp > outs_1_12/dr_const_1_12.out

echo
echo "Job finished. SLURM details are:"
echo
qstat -f ${SLURM_JOB_ID}
echo
echo Finished at `date`
