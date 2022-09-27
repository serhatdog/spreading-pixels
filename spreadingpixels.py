from numpy import zeros, uint8
from numba import jit

@jit
def resize(img, size):
    if size > 0:
        output_img = zeros((len(img)*size, len(img[0])*size, 3), uint8)
        for y in range(len(output_img)):
            for x in range(len(output_img[0])):
                output_img[y][x] = img[y//size][x//size]
        return output_img;
    elif size < 0:
        size*=-1
        output_img = zeros((len(img)//size, len(img[0])//size, 3), uint8)
        for y in range(len(output_img)):
            for x in range(len(output_img[0])):
                output_img[y][x] = img[y*size][x*size]
        return output_img;
    return img;

#Author: Serhat Dogan
#https://github.com/serhatdog/spreading-pixels
