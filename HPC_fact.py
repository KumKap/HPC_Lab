from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
fact = None
lower = None
upper = None
if rank == 0:
    fact = int(input("Enter any number: "))

fact = comm.bcast(fact, root=0)

if rank == 0:
    lower = 1
else:
    lower = rank * (fact // size) + 1

if rank == size - 1:
    upper = fact
else:
    upper = (rank + 1) * (fact // size)

# print(rank," has lower:",lower," and upper:", upper)
local_result = 1

for i in range(lower, upper + 1):
    local_result = local_result * i

print(rank," has lower:",lower," and upper:", upper, " and calculated:",local_result)


total = comm.reduce(local_result, op=MPI.PROD, root=0)

if rank == 0:
    print("Factorial of the number calculated using",size," processes is:",total)

#RUN: mpiexec -n 3 python -m mpi4py HPC_fact.py
# OUTPUT: Enter any number: 12
#
# 2  has lower: 9  and upper: 12  and calculated: 11880
# 1  has lower: 5  and upper: 8  and calculated: 1680
# 0  has lower: 1  and upper: 4  and calculated: 24
# Factorial of the number calculated using 3  processes is: 479001600
