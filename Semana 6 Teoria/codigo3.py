import matplotlib.pyplot as plt
from skimage import io
import matplotlib

image = io.imread('Semana 6 Teoria\imagem.png')

plt.hist(image[:,:,0].ravel(), bins=256, range=(0, 256), color='red', alpha=0.5)
plt.hist(image[:,:,1].ravel(), bins=256, range=(0, 256), color='green', alpha=0.5)
plt.hist(image[:,:,2].ravel(), bins=256, range=(0, 256), color='blue', alpha=0.5)

plt.title('Histograma')
plt.xlabel('Níveis de intensidade')
plt.ylabel('Frequência')

plt.show()