import cv2

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'haar-cascade-files-master/haarcascade_licence_plate_rus_16stages.xml')

while True:
    check,img = camera.read()
    imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGrey)
    #print(objetos)
    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2)

    cv2.imshow('Imagem',img)
    cv2.waitKey(1)