import cv2
import numpy as np

# carregando a imagem em escala de cinza
img = cv2.imread('semana10/imagem.png', 0)

# aplicando o operador de Prewitt
kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewittx_img = cv2.filter2D(img, -1, kernelx)
prewitty_img = cv2.filter2D(img, -1, kernely)
prewitt_img = cv2.addWeighted(prewittx_img, 0.5, prewitty_img, 0.5, 0)

# exibindo a imagem original e a imagem resultante
cv2.imshow('Imagem original', img)
cv2.imshow('Operador de Prewitt', prewitt_img)
cv2.imshow('Operador de Prewittx', prewittx_img)
cv2.imshow('Operador de Prewitty', prewitty_img)

cv2.waitKey(0)
cv2.imwrite('semana10/imagem_resultante_prewitt.png', prewitt_img)
cv2.imwrite('semana10/imagem_resultante_prewittx.png', prewittx_img)
cv2.imwrite('semana10/imagem_resultante_prewitty.png', prewitty_img)
cv2.destroyAllWindows()
