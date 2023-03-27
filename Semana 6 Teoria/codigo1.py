import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage import io, color

image = io.imread('Semana 6 Teoria\imagem.png')

gray_image = color.rgb2gray(image)
threshold_value = threshold_otsu(gray_image)

binary_image = gray_image > threshold_value
plt.imshow(binary_image, cmap='gray')
plt.show()