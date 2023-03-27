from skimage import io, exposure
import matplotlib.pyplot as plt
import matplotlib

# Carrega a imagem
image = io.imread('imagem.png')

# Equaliza o histograma da imagem
image_eq = exposure.equalize_hist(image)

# Mostra as imagens original e equalizada lado a lado
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))
ax1.imshow(image, cmap='gray')
ax1.set_title('Imagem original')
ax1.axis('off')
ax2.imshow(image_eq, cmap='gray')
ax2.set_title('Imagem equalizada')
ax2.axis('off')
plt.show()



