import cv2

# carrega o classificador Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# abre a câmera
cap = cv2.VideoCapture(0)

while True:
    # lê um frame da câmera
    ret, frame = cap.read()

    # converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecta faces no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # desenha um retângulo em volta de cada face detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # exibe o frame com as faces detectadas
    cv2.imshow('Detecção de Faces', frame)

    # espera pela tecla 'q' ser pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# libera a câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()
