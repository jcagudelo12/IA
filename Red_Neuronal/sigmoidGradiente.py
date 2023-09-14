#Importar numpy para uso de matrices
import numpy as np

#Importamos sigmoid
from sigmoid import sigmoid

def sigmoidGradiente(z):
    g = sigmoid(z)
    sig = np.multiply((g),(1 - g))
    return sig