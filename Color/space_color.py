import numpy as np
def convert_gray_scale(I):
    #Se crea una copia de la imagen original
    imagenTransformada = np.copy(I)
    #Se obtiene el tamaño de la imagen
    n,m = I.shape[0:2]


    img = np.zeros((m,n),dtype=np.uint8)

    #Se convierte en escala de grises
    for x in range(m):
        for y in range(n):
            img[x,y] = 0.299*imagenTransformada[x,y,0]+0.587*imagenTransformada[x,y,1]+0.114*imagenTransformada[x,y,2]
    return img