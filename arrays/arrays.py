import numpy

def arrays(arr):
    array = numpy.array(arr, dtype=float)
    reverse = numpy.flip(array)
    
    return reverse
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

