#include <mpi.h>

using namespace std;

int main(int argc, char** argv) {
  // Initialize MPI
  MPI_Init(&argc, &argv);

  // Get the rank and size of the communicator
  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  // Define the 2D array and the element to search for
  const int array_size = 3;
  int array[array_size][array_size] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  int element_to_search = 5;

  // Allocate a buffer to store the local row of the array
  int local_array[array_size];

  // Scatter the 2D array from the root process to all processes, such that each process receives one row
  MPI_Scatter(array, array_size, MPI_INT, local_array, array_size, MPI_INT, 0, MPI_COMM_WORLD);

  // Search for the element in the local row of the array
  bool element_found = false;
  for (int i = 0; i < array_size; i++) {
    if (local_array[i] == element_to_search) {
      element_found = true;
      break;
    }
  }

  // Gather the results from all processes to the root process
  int results[size];
  MPI_Gather(&element_found, 1, MPI_INT, results, 1, MPI_INT, 0, MPI_COMM_WORLD);

  // If the root process, check if the element was found in any rank.
  //If it was, print a message to the console. Otherwise, print a message saying that the element was not found in any rank.
  if (rank == 0) {
    bool element_found = false;
    for (int i = 0; i < size; i++) {
      if (results[i]) {
        element_found = true;
        break;
      }
    }

    if (element_found) {
      cout << "Element found in at least one rank." << endl;
    } else {
      cout << "Element not found in any rank." << endl;
    }
  }

  // Finalize MPI
  MPI_Finalize();

  return 0;
}
