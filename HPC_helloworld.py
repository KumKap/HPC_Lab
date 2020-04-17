from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print("Hello world from process:",rank," of:",size)


# RUN: mpiexec -n 4 python -m mpi4py HPC_helloworld.py
# OUTPUT
# Hello world from process: 2  of: 4
# Hello world from process: 1  of: 4
# Hello world from process: 0  of: 4
# Hello world from process: 3  of: 4

