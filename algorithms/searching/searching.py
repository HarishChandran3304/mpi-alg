from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

array = [[1,2,3],[4,5,6],[7,8,9]]
element_to_search = 5

rank = comm.Get_rank()
size = comm.Get_size()

chunk_size = int(len(array) / size)
start_index = rank * chunk_size
end_index = (rank + 1) * chunk_size

element_found = False
for i in range(start_index, end_index):
    for j in range(len(array[0])):
        if array[i][j] == element_to_search:
            element_found = True
            break

if element_found:
    print("Element found in rank {} at index ({}, {})".format(rank, i, j))

results = comm.gather(element_found, root=0)

if rank == 0:
    if any(results):
        print("Element found in at least one rank.")
    else:
        print("Element not found in any rank.")
