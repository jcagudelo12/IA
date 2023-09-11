import numpy as np

def sigmoid(z):
    row = z.shape[0]
    g = np.zeros((row, z.shape[1]))
    for i in range(row):
        g[i,0] = 1 / (1 + np.exp(-z[i]))      
    return g