# Imports
from example_binary_tree import root
from traversal import parallel_tree_traversal
from mpi4py import MPI


# Seting up MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# Main function
def main():
    try:
        parallel_tree_traversal(root, rank, size)
    except:
        pass


# Main call
if __name__ == "__main__":
    main()