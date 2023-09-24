from Binarización import bersen
from Color import space_color
import cv2 as cv
import matplotlib.pyplot as plt
''' img = cv.imread('person_bacteria.jpeg',cv.IMREAD_GRAYSCALE)
img2 = BersenThreshold(img,13,30,210) /'''

if __name__ == "__main__":
    # Lectura de imágenes
    img1 = cv.imread("carretera.jpg",cv.IMREAD_GRAYSCALE)
    img2 = cv.imread("image-cell.png",cv.IMREAD_GRAYSCALE)
    img3 = cv.imread("person_bacteria.jpeg",cv.IMREAD_GRAYSCALE)
    # Umbralizacion adaptativa
    img1B = bersen.BersenThreshold(img1,2,60,136)
    img2B = bersen.BersenThreshold(img2,2,45,240,2)
    img3B = bersen.BersenThreshold(img3,11,40,200)
    plt.figure(1,figsize=(8,8))
    plt.subplot(3,4,1)
    plt.imshow(img1,cmap="gray")
    plt.axis("off")
    plt.title("Imagen original")
    plt.subplot(3,4,2)
    plt.axis("off")
    plt.title("Umbralización Bernsen")
    plt.imshow(img1B,cmap="gray")
    plt.subplot(3,4,3)
    plt.axis("off")
    plt.subplot(3,4,5)
    plt.imshow(img2,cmap="gray")
    plt.axis("off")
    plt.title("Imagen original")
    plt.subplot(3,4,6)
    plt.axis("off")
    plt.title("Umbralización Bernsen")
    plt.imshow(img2B,cmap="gray")
    plt.subplot(3,4,6)
    plt.axis("off")
    plt.subplot(3,4,9)
    plt.axis("off")
    plt.imshow(img3,cmap="gray")
    plt.axis("off")
    plt.title("Imagen original")
    plt.subplot(3,4,10)
    plt.imshow(img3B,cmap="gray")
    plt.axis("off")
    plt.title("Umbralización Bernsen")
    plt.show()

