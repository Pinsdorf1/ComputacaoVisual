from skimage import io, exposure
import matplotlib.pyplot as plt
import matplotlib

image = io.imread('Semana 6 Teoria\imagem.png')
image_eq = exposure.equalize_hist(image)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))
ax1.imshow(image, cmap='gray')
ax1.set_title('Imagem original')
ax1.axis('off')
ax2.imshow(image_eq, cmap='gray')
ax2.set_title('Imagem equalizada')
ax2.axis('off')
plt.show()