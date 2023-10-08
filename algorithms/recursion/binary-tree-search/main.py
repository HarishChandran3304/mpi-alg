# Imports
from example_binary_tree import root
from search import parallel_tree_search
from mpi4py import MPI


# Main function
def main():
    # Seting up MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Running the parallel binary tree search algorithm
    try:
        parallel_tree_search(root, 11, rank, size)
    except:
        pass


# Main call
if __name__ == "__main__":
    main()