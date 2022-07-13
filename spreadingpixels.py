import numpy as np
from numba import jit

@jit
def resize(oI, size):
    pI = np.zeros((len(oI)*size, len(oI[0])*size, 3), np.uint8)
    for x in range(len(pI)):
        for y in range(len(pI[0])):
            pI[y][x] = oI[y//size][x//size]
    return pI

#Author: Serhat Dogan
#https://github.com/serhatdog/spreading-pixels