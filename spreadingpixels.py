import numpy as np
from numba import jit

@jit
def resize(oI, size):
    
    if size > 0:

        pI = np.zeros((len(oI)*size, len(oI[0])*size, 3), np.uint8)
        for y in range(0, len(pI), 1):
            for x in range(0, len(pI[0]), 1):
                pI[y][x] = oI[y//size][x//size]
        return pI

    elif size < 0:
        
        size *= -1 
        pI = np.zeros((len(oI)//size, len(oI[0])//size, 3), np.uint8)
        for y in range(0, len(oI)):
            for x in range(0, len(oI[0])):
                pI[y//size][x//size] = oI[y][x]
        return pI

    return oI

#Author: Serhat Dogan
#https://github.com/serhatdog/spreading-pixels
