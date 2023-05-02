import cv2

# Carregar o classificador Haar Cascade pré-treinado para detecção de rosto humano
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Carregar a imagem PNG
img = cv2.imread('asd.jpeg')

# Converter a imagem para escala de cinza para processamento mais fácil
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar faces na imagem usando o Haar Cascade
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Desenhar um retângulo ao redor da(s) face(s) detectada(s)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Exibir a imagem com as faces detectadas
cv2.imshow('Imagem com detecção de face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
