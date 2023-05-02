import cv2

# carrega o classificador Haar Cascade para gatos
cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

# carrega a imagem em escala de cinza
img = cv2.imread('asd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecta gatos na imagem
cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# desenha um retângulo em volta de cada gato detectado
for (x, y, w, h) in cats:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# exibe a imagem com os retângulos desenhados
cv2.imshow('Gatos Detectados', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
