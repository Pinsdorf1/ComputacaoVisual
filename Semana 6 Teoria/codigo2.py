import matplotlib.pyplot as plt
import matplotlib
from skimage import io, color

# Carrega a imagem em escala de cinza
image = color.rgb2gray(io.imread('imagem.png'))

# Plota o histograma
plt.hist(image.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

# Define o título e os rótulos dos eixos
plt.title('Histograma da imagem')
plt.xlabel('Níveis de cinza')
plt.ylabel('Frequência')

# Exibe o histograma
plt.show()

