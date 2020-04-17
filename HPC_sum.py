from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
num = None
lower = None
upper = None
if rank == 0:
    num = int(input("Enter any number: "))

num = comm.bcast(num, root=0)

if rank == 0:
    lower = 1
else:
    lower = rank * (num // size) + 1

if rank == size - 1:
    upper = num
else:
    upper = (rank + 1) * (num // size)

local_result = 0

for i in range(lower, upper + 1):
    local_result = local_result + i

print(rank," has lower:",lower," and upper:", upper, " and calculated:",local_result)

total = comm.reduce(local_result, op=MPI.SUM, root=0)

if rank == 0:
    print("Sum of numbers upto:",num," by using:",size," processes is:",total)

#RUN: mpiexec -n 3 python -m mpi4py HPC_sum.py
#OUTPUT: Enter any number: 24
#
# 2  has lower: 17  and upper: 24  and calculated: 164
# 1  has lower: 9  and upper: 16  and calculated: 100
# 0  has lower: 1  and upper: 8  and calculated: 36
# Sum of numbers upto: 24  by using: 3  processes is: 300
