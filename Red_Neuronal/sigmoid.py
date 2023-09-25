#Importar numpy para uso de matrices
from math import exp
import numpy as np

def sigmoid(z):
    row = z.size
    g = np.zeros(row)
    for i in range(row):
        ed = np.exp(-z[i])
        fil = 1/(1+ed)
        g[i] = fil
    return g
