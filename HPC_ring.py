from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
token = None
if rank != 0:
    data = comm.recv(source=(rank - 1))
    print("Process:",rank," received token:",token," from process:",rank-1)

else:
    token = -1

comm.send(token, dest=((rank + 1) % size) )

if rank == 0:
    token = comm.recv(source=(size - 1))
    print("Process:",rank," received token:",token," from process:",size-1)


# RUN: mpiexec -n 4 python -m mpi4py HPC_ring.py
# OUTPUT
# Process: 1  received token: None  from process: 0
# Process: 2  received token: None  from process: 1
# Process: 3  received token: None  from process: 2
# Process: 0  received token: None  from process: 3

