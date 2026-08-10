# [Arrays](https://www.hackerrank.com/challenges/np-arrays/problem)

## Problem Statement
A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.

**Task**
You are given a space-separated list of numbers. Your task is to print a reversed NumPy array with the element type `float`.

### Input Format
A single line of input containing space-separated numbers.

### Output Format
Print the reverse NumPy array with type `float`.

### Sample Input
```text
1 2 3 4 -8 -10
```

### Sample Output
```text
[-10.  -8.   4.   3.   2.   1.]
```

***

## Optimization Tricks Implemented

### 1. Element Type Casting (`float`)
Instead of parsing the string inputs into floats manually via a loop or mapping function before creating the array, NumPy allows you to specify the element type directly inside the initialization function. Passing `float` or `dtype=float` as the secondary parameter instantly converts all element values into float objects during array creation.
```python
# Efficient shorthand type conversion
numpy.array(your_list, float)
```

### 2. Multi-Dimensional Flip Engine (`np.flip()`)
While basic Python list slicing (`[::-1]`) works for 1D structural spaces, utilizing the native `np.flip()` method is a far superior framework for scaling. 
* **Vector Optimization:** `np.flip()` reverses the order of elements along a specified axis without creating a heavy nested memory block copies.
* **Scalability:** This solution seamlessly adapts when transitioning from 1D data arrays to complex 2D or 3D matrices later in the course.
