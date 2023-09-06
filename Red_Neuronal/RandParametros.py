#Importar numpy para uso de matrices
import numpy as np

def randParametros(lIn,lOut):
    w = np.zeros((lIn,lOut))
    epsilon = 0.12
    w = (np.random.rand(lOut, (1 + lIn))) * 2 * epsilon - epsilon
    return w