import cv2
import numpy as np

# carregando a imagem em escala de cinza
img = cv2.imread('semana10/imagem.png', 0)

# aplicando o operador de Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_img = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# exibindo a imagem original e a imagem resultante
cv2.imshow('Imagem original', img)
cv2.imshow('x', sobelx)
cv2.imshow('y', sobely)
cv2.imshow('Operador de Sobel', sobel_img)
cv2.waitKey(0)
cv2.imwrite('semana10/imagem_resultante_sobel.png', sobel_img)
cv2.imwrite('semana10/imagem_resultante_sobelx.png', sobelx)
cv2.imwrite('semana10/imagem_resultante_sobely.png', sobely)
cv2.destroyAllWindows()