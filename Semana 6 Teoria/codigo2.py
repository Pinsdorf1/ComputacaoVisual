import matplotlib.pyplot as plt
import matplotlib
from skimage import io, color

image = color.rgb2gray(io.imread('Semana 6 Teoria\imagem.png'))
matplotlib.image.imsave('Semana 6 Teoria\imagem2.png', image)

plt.hist(image.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

plt.title('Histograma')
plt.xlabel('Níveis de cinza')
plt.ylabel('Frequência')

plt.show()

