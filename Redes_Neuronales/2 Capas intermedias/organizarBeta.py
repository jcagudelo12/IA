import numpy as np
def organizarBeta(tamano_capa_media_1, tamano_capa_media_2, tamano_capa_entrada, num_salidas, parametros_Beta):
    cont = 0
    NumCol1 = tamano_capa_entrada + 1
    NumFil1 = tamano_capa_media_1

    NumCol2 = tamano_capa_media_1 + 1
    NumFil2 = tamano_capa_media_2

    NumCol3 = tamano_capa_media_2 + 1
    NumFil3 = num_salidas

    Beta1 = np.zeros((NumFil1,NumCol1))
    Beta2 = np.zeros((NumFil2,NumCol2))
    Beta3 = np.zeros((NumFil3,NumCol3))

    lens = len(parametros_Beta)
    if lens != 10935:
        parametros_Beta = parametros_Beta[0]
    for i in range(NumFil1):
      for j in range(NumCol1):
        Beta1[i,j] = parametros_Beta[cont,0]
        cont = cont + 1

    for i in range(NumFil2):
      for j in range(NumCol2):
        Beta2[i,j] = parametros_Beta[cont,0]
        cont = cont + 1

    for i in range(NumFil3):
      for j in range(NumCol3):
          Beta3[i,j] = parametros_Beta[cont,0]
        cont = cont + 1

    return(Beta1, Beta2, Beta3)