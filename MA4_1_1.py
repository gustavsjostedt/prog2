
"""
Solutions to module 4
Review date:
"""

student = "Gustav Sjöstedt Eriksson"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):
    # Write your code here
    coord_list = []
    in_circle = []
    
    for _ in range(n):
        x, y = 2*r.random() - 1, 2*r.random() - 1
        coord_list.append((x, y))
    
    for coordinate in coord_list:
         if coordinate[0]**2 + coordinate[1]**2 <= 1:
              in_circle.append(coordinate)

    pi = 4*len(in_circle)/len(coord_list)

    plt.scatter(*zip(*in_circle), c='red', s=1)
    outside_coord = [(x, y) for x, y in coord_list if x**2 + y**2 > 1]
    plt.scatter(*zip(*outside_coord), c = 'blue', s = 1)

    plt.gca().set_aspect('equal')
    plt.show()

    return pi

def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
        #plot(n)

if __name__ == '__main__':
	main()
