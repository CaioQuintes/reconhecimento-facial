import cv2
import serial

# Inicialize a comunicação serial com o Arduino
ser = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

# Carregue o Haarcascade para detecção de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicialize a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Calcule as coordenadas do centro do rosto
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # Envie as coordenadas para o Arduino
        ser.write(f"{face_center_x},{face_center_y}\n".encode())

        # Desenhe um retângulo ao redor do rosto
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Exiba o vídeo com os retângulos desenhados
    cv2.imshow('Face Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()