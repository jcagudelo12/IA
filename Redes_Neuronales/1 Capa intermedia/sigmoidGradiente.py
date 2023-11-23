#Importar numpy para uso de matrices
import numpy as np

#Importamos sigmoid
from sigmoid import sigmoid

def sigmoidGradiente(z):
    sig = np.multiply((sigmoid(z)),(1-sigmoid(z)))
    return sig