import numpy as np
from numba import jit

@jit
def resize_up(oI, size):
    pI = np.zeros((len(oI)*size, len(oI[0])*size, 3), np.uint8)
    for y in range(0, len(pI), 1):
        for x in range(0, len(pI[0]), 1):
            pI[y][x] = oI[y//size][x//size]
    return pI

@jit
def resize_down(oI, size):
    pI = np.zeros((len(oI)//size, len(oI[0])//size, 3), np.uint8)
    for y in range(0, len(oI)):
        for x in range(0, len(oI[0])):
            pI[y//size][x//size] = oI[y][x]
    return pI

#Author: Serhat Dogan
#https://github.com/serhatdog/spreading-pixels
