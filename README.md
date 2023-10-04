# mpi-alg
DSA algorithms implemented using parallel computing and MPI (Message Passing Interface) to enhance performance.

## Steps to run locally
1) Make sure you have OpenMPI installed on your system. If not, follow the instructions [here](https://www.open-mpi.org/software/ompi/v4.1/).

2) Clone the repository:
```bash
$ git clone https://github.com/HarishChandran3304/mpi-alg.git
```

3) Change directory to the repository:
```bash
$ cd mpi-alg
```

4) Create a virtual environment:
```bash
$ python3 -m venv venv
```

5) Activate the virtual environment:
```bash
$ source ./venv/bin/activate
```

6) Install the dependencies:
```bash
$ pip install -r requirements.txt
```

7) Navigate to the directory of the algorithm you want to run:
```bash
$ cd algorithms/<algorithm-type>
```

8) Run the algorithm with the recommended number of processes:
```bash
$ mpiexec -n <number-of-processes> python3 <algorithm-name>.py
```