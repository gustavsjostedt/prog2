
"""
Solutions to module 4
Review date:
"""

student = "Gustav Sjöstedt Eriksson"
reviewer = ""

import math as m
import random as r


def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    x_coords = []
    for _ in range(n):
        x_coords.append(tuple(r.uniform(-1, 1) for _ in range(d)))

    in_hs =  list(filter(lambda tup: sum(x**2 for x in tup) <= 1, x_coords))

    return len(in_hs)/len(x_coords) * 2**d
    

    '''x_list = []
    for _ in range(n): 
        
        for _ in range(d):
            [x for x in range(d)]  
        #res = sum(map((lambda x: x**2, x_list)))'''
 
         


    print(in_hs)






    return 

def hypersphere_exact(n,d):
    volume = m.pi**(d/2)/(m.gamma(d/2 + 1))
    return volume
     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)


if __name__ == '__main__':
	main()
