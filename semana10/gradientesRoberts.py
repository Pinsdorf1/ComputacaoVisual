import cv2
import numpy as np

# carregando a imagem em escala de cinza
img = cv2.imread('semana10/imagem.png', 0)

# aplicando o operador de Roberts
kernelx = np.array([[1, 0], [0, -1]])
kernely = np.array([[0, 1], [-1, 0]])
robertsx_img = cv2.filter2D(img, -1, kernelx)
robertsy_img = cv2.filter2D(img, -1, kernely)
roberts_img = cv2.addWeighted(robertsx_img, 0.5, robertsy_img, 0.5, 0)

# exibindo os filtros horizontais e verticais
cv2.imshow('Filtro horizontal', robertsx_img)
cv2.imshow('Filtro vertical', robertsy_img)
cv2.imshow('Operador de Roberts', roberts_img)
cv2.waitKey(0)
cv2.imwrite('semana10/imagem_resultante_roberts.png', roberts_img)
cv2.imwrite('semana10/imagem_resultante_robertsx.png', robertsx_img)
cv2.imwrite('semana10/imagem_resultante_robertsy.png', robertsy_img)
cv2.destroyAllWindows()