from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data_for_one = 101
    data_for_two = 10101
    comm.send(data_for_one, dest=1, tag=1)
    comm.send(data_for_two, dest=2, tag=1)
elif rank == 1:
    data = comm.recv(source=0, tag=1)
    print("Data received by",rank," from process 0:",data)
    data_for_two = 20101
    comm.send(data_for_two, dest=2)
elif rank == 2:
    data = comm.recv(source=0, tag=1)
    print("Data received by",rank," from process 1:",data)
    data = comm.recv(source=1)
    print("Data received by",rank," from process 2:",data)

# RUN: mpiexec -n 3 python -m mpi4py HPC_sendrec.py
# OUTPUT
# Data received by 1  from process 0: 101
# Data received by 2  from process 1: 10101
# Data received by 2  from process 2: 20101

