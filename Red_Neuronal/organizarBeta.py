import numpy as np
def organizarBeta(tamano_capa_media,tamano_capa_entrada,num_salidas,parametros_Beta):
    cont = 0
    NumCol1 = tamano_capa_entrada + 1
    NumFil1 = tamano_capa_media

    NumCol2 = tamano_capa_media + 1
    NumFil2 = num_salidas


    Beta1 = np.zeros((NumFil1,NumCol1))
    Beta2 = np.zeros((NumFil2,NumCol2))
    
    lens = len(parametros_Beta)
    if lens != 10285:
        parametros_Beta = parametros_Beta[0]
    for i in range(NumFil1):
        for j in range(NumCol1):
            Beta1[i,j] = parametros_Beta[cont,]
            cont = cont+1

    for i in range(NumFil2):
        for j in range(NumCol2):
            Beta2[i,j] = parametros_Beta[cont,]
            cont = cont+1

        
    return(Beta1,Beta2)