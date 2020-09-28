#!/bin/sh

# Name of job
#SBATCH -J $FILEBASE_$ID

# Walltime limit (hours:mins:secs)
#SBATCH -t 24:00:00

# Nodes and procs
#SBATCH -N 1
#SBATCH -n 1


# Standard error and out files
#SBATCH -o outs_$ID/$FILEBASE_$ID.o
#SBATCH -e outs_$ID/$FILEBASE_$ID.e

module unload gcc
module load gcc/6.2.0

echo "Starting job $SLURM_JOB_ID"

export LD_LIBRARY_PATH=~/lib:$LD_LIBRARY_PATH
export PATH=~/bin/$PATH
mkdir -p outs_$ID

# Main job
~/LatticeDNAOrigami/bin/latticeDNAOrigami -i $FILEBASE_$ID.inp > outs_$ID/$FILEBASE_$ID.out

echo
echo "Job finished. SLURM details are:"
echo
qstat -f ${SLURM_JOB_ID}
echo
echo Finished at `date`
