#!/usr/bin/env bash
#SBATCH --job-name=PPQ3               # Job name
#SBATCH --nodes=1                       # Number of nodes to run on
#SBATCH --ntasks=20                      # Number of MPI tasks to request
#SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
#SBATCH --mem=16G                       # Total memory to request
#SBATCH --time=0-00:00:10               # Time limit (DD-HH:MM:SS)
#SBATCH --account=dept-proj-year        # Project account to use
#SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=qnz500@york.ac.uk   # Where to send mail
#SBATCH --output=%x-%j.log              # Standard output log
#SBATCH --error=%x-%j.err               # Standard error log
#SBATCH --partition=test

#actual executable info now:
EXEC="./a.out"

#tell user what is going on:
echo My working directory is `pwd`
echo Running job on host:
echo -e '\t'`hostname` at `date`
echo -e '\t'using $SLURM_NTASKS MPI tasks
echo

srun --mpi=pmix -n ${SLURM_NTASKS} $EXEC

echo
echo Job completed at `date`
