import numpy as np
from .heaviside import heaviside

def rect_array(arr:np.ndarray,lims=(-1/2,1/2)):
    result = np.zeros(arr.size)
    for i,x in enumerate(arr):
        result[i] = rect(x,lims)
    return result



def rect(x,lims=(-1/2,1/2)):
    range = abs(lims[0]) + abs(lims[1])
    return (heaviside(x,center=lims[0]) - heaviside(x,center=lims[1])) / range

