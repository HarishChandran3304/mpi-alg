# Imports
from algorithms.recursion.example_binary_tree import root
from traversal import parallel_tree_traversal
from mpi4py import MPI


# Main function
def main():
    # Seting up MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Running the parallel tree traversal algorithm
    try:
        parallel_tree_traversal(root, rank, size)
    except:
        pass


# Main call
if __name__ == "__main__":
    main()