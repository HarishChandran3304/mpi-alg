#include <stdio.h> 
#include <stdlib.h> 
#include <mpi.h> 
#include <math.h> 
#include <stdbool.h> 
#define SIZE 1000

//MPI timer var
double start_timer;
double finish_timer;
//Merge Function
void merge (int *first, int *second, int *result, int first_size, int second_size){
  int i = 0;
  int j = 0;
  int k = 0;
  while (i < first_size && j < second_size){
      if (first[i] < second[j]){
          result[k] = first[i];
          k++;
          i++;
          
      }
      else{
          result[k] = second[j];
          k++;
          j++;
      }
      if (i == first_size){
          while (j < second_size){
              result[k] = second[j];
              k++;
              j++;
          }
      }
      else if (j == second_size){
          while (i < first_size){
              result[k] = first[i];
              i++;
              k++;
          }
      }
  }
}

//Partition Function
int partitionArray (int *arr, int low, int high){
    int middle = floor ((low + high) / 2);
    int pivot = arr[middle];
    int j, temp;
    temp = arr[middle];
    arr[middle] = arr[high];
    arr[high] = temp;
    int i = (low - 1);
    for (j = low; j <= high - 1; j++){
        if (arr[j] < pivot){
            i++;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}

//Quicksort function
void quicksort (int *number, int first, int last){
    if (first < last){
        int pivot_index = partitionArray (number, first, last);
        quicksort (number, first, pivot_index - 1);
        quicksort (number, pivot_index + 1, last);
    }
}

//Main function
int main (int argc, char *argv[]){
    int *unsorted_array = (int *) malloc (SIZE * sizeof (int));
    int *result = (int *) malloc (SIZE * sizeof (int));
    
    int array_size = SIZE;
    int size, rank;
    int sub_array_size;

//Setting up MPI process
    MPI_Status status;
    MPI_Init (&argc, &argv);
    MPI_Comm_rank (MPI_COMM_WORLD, &rank); //Returning process rank
    MPI_Comm_size (MPI_COMM_WORLD, &size); //Returning total number of processes
//MPI_COMM_WORLD is the default communicator, contains all processes available for use

//Generating 1000 random numbers
    if (rank == 0){
        printf ("Unsorted array: ");
        int j = 0;
        for (j = 0; j < SIZE; ++j){
            unsorted_array[j] = (int) rand () % 100;
            printf ("%d ", unsorted_array[j]);
        }
        printf ("\n\n");
    }
    int iter_count = size;
    sub_array_size = (int) SIZE / iter_count;
    if (rank == 0){
        start_timer = MPI_Wtime ();
        int i = 0;
        if (iter_count > 1){
            for (i = 0; i < iter_count - 1; i++){
                int j;
                MPI_Send (&unsorted_array[(i + 1) * sub_array_size],
                sub_array_size, MPI_INT, i + 1, 0, MPI_COMM_WORLD);
            }
            int i = 0;
            int *sub_array = (int *) malloc (sub_array_size * sizeof (int));
            for (i = 0; i < sub_array_size; i++){
                sub_array[i] = unsorted_array[i];
            }
            quicksort (sub_array, 0, sub_array_size - 1);
            for (i = 0; i < iter_count; i++){
                if (i > 0){
                    int temp_sub_array[sub_array_size];
                    MPI_Recv (temp_sub_array, sub_array_size, MPI_INT, i, 777,
                    MPI_COMM_WORLD, &status); //checks overflow error
                    int j;
                    int temp_result[i * sub_array_size];
                    for (j = 0; j < i * sub_array_size; j++){
                        temp_result[j] = result[j];
                    }
                    int temp_result_size = sub_array_size * i;
                    merge (temp_sub_array, temp_result, result, sub_array_size,
                    temp_result_size);
                }
                else{
                    int j;
                    for (j = 0; j < sub_array_size; j++){
                        result[j] = sub_array[j];
                    }
                    free (sub_array);
                }
            }
        }
        else{
            quicksort (unsorted_array, 0, SIZE - 1);
            for (i = 0; i < SIZE; i++){
                result[i] = unsorted_array[i];
            }
        }
        finish_timer = MPI_Wtime ();
    }
    else{
        sub_array_size = (int) SIZE / iter_count;
        int *sub_array = (int *) malloc (sub_array_size * sizeof (int));
        MPI_Recv (sub_array, sub_array_size, MPI_INT, 0, 0,
		MPI_COMM_WORLD, &status);
        quicksort (sub_array, 0, sub_array_size - 1);
        int i = 0;
        MPI_Send (sub_array, sub_array_size, MPI_INT, 0, 777, MPI_COMM_WORLD);
        free (sub_array);
    }
  if (rank == 0){
      bool error = false;
      int i = 0;
      for (i = 0; i < SIZE - 1; i++){
          if (result[i] > result[i + 1]){
              error = true;
              printf ("Error!\n", i);
          }
      }
      if (error)
      printf ("Error occured, array not sorted correctly\n");
      else{
          printf ("Sorted array: ");
          for (int q = 0; q < SIZE; q++){
              printf ("%d ", result[q]);
          }
          printf ("\n\n");
          printf ("Execution time: %2.6fs \n", finish_timer - start_timer);
      }
  }
  free (unsorted_array);
  MPI_Finalize ();
}
