import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage import io, color

# Carrega a imagem
image = io.imread('imagem.png')

# # Exibe a imagem original
# plt.imshow(image)
# plt.show()

# Converte a imagem para escala de cinza e calcula o valor de limiar
gray_image = color.rgb2gray(image)
threshold_value = threshold_otsu(gray_image)

# Aplica a limiarização à imagem e exibe o resultado
binary_image = gray_image > threshold_value
plt.imshow(binary_image, cmap='gray')
plt.show()
