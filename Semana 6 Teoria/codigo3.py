import matplotlib.pyplot as plt
from skimage import io
import matplotlib

# Carrega a imagem
image = io.imread('imagem.png')

# Plota o histograma para cada canal de cor
plt.hist(image[:,:,0].ravel(), bins=256, range=(0, 256), color='red', alpha=0.5)
plt.hist(image[:,:,1].ravel(), bins=256, range=(0, 256), color='green', alpha=0.5)
plt.hist(image[:,:,2].ravel(), bins=256, range=(0, 256), color='blue', alpha=0.5)

# Define o título e os rótulos dos eixos
plt.title('Histograma da imagem')
plt.xlabel('Níveis de intensidade')
plt.ylabel('Frequência')

# Exibe o histograma
plt.show()


