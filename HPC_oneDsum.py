from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = None
numpy_arr = None
elements_per_process = None
arr = [75,91,6,10,25,64,32,5,10,22,41,17,38,11,67,99,3,52,77]
l = None
if size == 1:
    print("Sum of all number by 1 process is:",sum(arr))
else:
    if rank == 0:
        l = len(arr)
        if l % size != 0: #pad extra 0 for unequal division of data among the processes
            temp = l % size
            temp = size - temp
            pad = [0] * temp
            arr = arr + pad
            l = l + temp
        elements_per_process = l // size
        numpy_arr = np.array(arr, dtype="i").reshape(size,elements_per_process)
        #convert arr into multidimensional array to scatter data equally such that
        #each process receives one dimension each

    data = comm.scatter(numpy_arr, root=0)

    local_sum = 0
    for i in data:
        local_sum += i
    print("Process:",rank," has data:",data," and partial sum calculated is:",local_sum)

    total = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        print("Sum of numbers by using:",size," processes is:",total)

#RUN: mpiexec -n 1 python -m mpi4py HPC_oneDsum.py
# OUTPUT:Sum of all number by 1 process is: 745
#
# RUN: mpiexec -n 7 python -m mpi4py HPC_oneDsum.py
#  OUTPUT: Process: 6  has data: [77  0  0]  and partial sum calculated is: 77
# Process: 5  has data: [99  3 52]  and partial sum calculated is: 154
# Process: 3  has data: [22 41 17]  and partial sum calculated is: 80
# Process: 4  has data: [38 11 67]  and partial sum calculated is: 116
# Process: 2  has data: [32  5 10]  and partial sum calculated is: 47
# Process: 0  has data: [75 91  6]  and partial sum calculated is: 172
# Sum of numbers by using: 7  processes is: 745
# Process: 1  has data: [10 25 64]  and partial sum calculated is: 99



