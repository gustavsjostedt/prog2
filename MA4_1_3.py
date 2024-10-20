
"""
Solutions to module 4
Review date:
"""

student = "Gustav Sjöstedt Eriksson"
reviewer = ""

import math as m
import random as r

from time import perf_counter as pc
from concurrent.futures import as_completed
import concurrent.futures as future


def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    x_coords = []
    for _ in range(n):
        x_coords.append(tuple(r.uniform(-1, 1) for _ in range(d)))

    in_hs =  list(filter(lambda tup: sum(x**2 for x in tup) <= 1, x_coords))
    vol = len(in_hs)/len(x_coords) * 2**d

    return vol


def hypersphere_exact(n,d):
    volume = m.pi**(d/2)/(m.gamma(d/2 + 1))
    return volume


# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function  

    results = []
    with future.ProcessPoolExecutor() as ex:
        p = [ex.submit(sphere_volume, n, d) for _ in range(np)] 
        for process in future.as_completed(p):
            result = process.result()
            results.append(result)
    return sum(results)/np

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):

    results = []

    with future.ProcessPoolExecutor() as ex:
        p = [ex.submit(sphere_volume, n//np, d) for _ in range(np)] 
        for process in future.as_completed(p):
            result = process.result()
            results.append(result)
    return sum(results)/np

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    end = pc()
    print(f'Det tog {end-start} s att köra sphere_volume 10 gånger')
    

    start = pc()
    sphere_volume_parallel1( n, d, 10)
    end = pc()
    print(f'Tiden för parallell_1 tog {end-start} s')

    start = pc()
    sphere_volume_parallel2( n, d, 10)
    end = pc()
    print(f'Tiden för parallell_2 tog {end-start} s')
    
    


if __name__ == '__main__':
	main()
