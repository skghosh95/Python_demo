Create and run processes
# We create a process with multiprocessing.Process(). It takes two important arguments:

# target: a callable object (function) for this process to be invoked when the process starts
# args: the (function) arguments for the target function. This must be a tuple
# Start a process with process.start()

# Call process.join() to tell the program that it should wait for this process to complete before it continues with the rest of the code.

from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choise for the number of processes

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main programm until these processes are finished
    for process in processes:
        process.join()




Process Pools
# A process pool object controls a pool of worker processes to which jobs can be submitted It supports asynchronous results with timeouts and callbacks and
# has a parallel map implementation.
from multiprocessing import Pool 

def cube(number):
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool()

    # by default this allocates the maximum number of available 
    # processors for this task --> os.cpu_count()
    result = p.map(cube,  numbers)
    
    # or 
    # result = [p.apply(cube, args=(i,)) for i in numbers]
    
    p.close()
    p.join()
    
    print(result)

Outside:
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


