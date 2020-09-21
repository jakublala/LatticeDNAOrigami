#!/bin/sh

# Name of job
#SBATCH -J sr_const_0

# Walltime limit (hours:mins:secs)
#SBATCH -t 24:00:00

# Nodes and procs
#SBATCH -n 5

# Standard error and out files
#SBATCH -o outs_0/sr_const_0.o
#SBATCH -e outs_0/sr_const_0.e

module unload gcc
module load gcc/6.2.0

echo "Starting job $SLURM_JOB_ID"

export LD_LIBRARY_PATH=~/lib:$LD_LIBRARY_PATH
export PATH=~/bin/$PATH
mpirun -n 5 mkdir -p outs_0/

# Main job
mpirun -n 5 ~/LatticeDNAOrigami/bin/latticeDNAOrigami -i sr_const_0.inp > outs_0/sr_const_0.out

echo
echo "Job finished. SLURM details are:"
echo
qstat -f ${SLURM_JOB_ID}
echo
echo Finished at `date`
