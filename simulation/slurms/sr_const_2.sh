#!/bin/sh

# Name of job
#SBATCH -J ../configs/sr_const_2

# Walltime limit (hours:mins:secs)
#SBATCH -t 5:00:00

# Nodes and procs
#SBATCH -N 1
#SBATCH -n 1

mkdir -p ../outs/2
# Standard error and out files
#SBATCH -o ../outs/2/sr_const_$ID.o
#SBATCH -e ../outs/2/sr_const_$ID.e

module unload gcc
module load gcc/6.2.0

echo "Starting job $SLURM_JOB_ID"

export LD_LIBRARY_PATH=~/lib:$LD_LIBRARY_PATH
export PATH=~/bin/$PATH

# Main job
~/LatticeDNAOrigami/bin/latticeDNAOrigami -i ../configs/sr_const_2.inp > ../outs/$ID/sr_const_$ID.out

echo
echo "Job finished. SLURM details are:"
echo
qstat -f ${SLURM_JOB_ID}
echo
echo Finished at `date`
