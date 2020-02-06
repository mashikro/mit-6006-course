# For which values of n does insertion sort beat merge sort?
# insertion_sort = 8*n^2 or merge_sort = 64*n*log n
import math

def find_faster_sort():

    for n in range(1, 10000):
        insertion_sort = 8*(n**2) 
        merge_sort = 64*n*math.log2(n)
        
        if insertion_sort <= merge_sort:
            print('Here:', n)

find_faster_sort()

# Ans: up until n=43 insertion sort is faster which makes sense as insertion sort is faster for smaller n.