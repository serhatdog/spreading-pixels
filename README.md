![alt text](https://github.com/serhatdog/spreading-pixels/blob/main/repo.png?raw=true)

## How the function works?
**The function has two paramaters:** *resize(oI, size)*
  1. Original Image (OpenCV & Numpy Array)
  2. Size (Original Image Res. x Size)
 
 **Creating new image:** *Using Numpy*
 
 **pI*: Processed Image, **oI*: Original Image
 
Preparing a canvas for a newly enlarged image using the zeros module from the numpy library.
 
The dimensions of the original image are multiplied by the value entered as a parameter and resized

**Spreading pixels:** *copying pixels on the x and y axes*

We know that there is a numpy array in the original image in which the color values are stored, so with the help of a simple form loop; numpy arrays are shared on the new image by jumping 1 time on the x & x+1 and y & y+1 axes.

## Why We Have To Use Numba?

Numba translates Python functions to optimized machine code at runtime using the industry-standard LLVM compiler library. Numba-compiled numerical algorithms in Python can approach the speeds of C or FORTRAN.

You don't need to replace the Python interpreter, run a separate compilation step, or even have a C/C++ compiler installed. Just apply one of the Numba decorators to your Python function, and Numba does the rest.
