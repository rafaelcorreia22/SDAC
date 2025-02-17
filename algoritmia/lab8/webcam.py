import cv2 as cv

webcam = cv.VídeoCapture(0)

if not webcam.isOpend():
  print("It's ok")
  exit() 

while True:
  retorno, frame = webcam.read()

  if not retorno:
    print("Erro na captura da webcam")
    break

  frameTonsCinza = cv.cvtColor(frame. cv.COLOR_BGR2GRAY)

  cv.imshow('Image original', frame)
  cv.inshow('Imagem capturada pela webcam.frame')

  if cv.waitKey(1) == ord('q'):
    break 

webcam.release()
cv.destroyAllWindows()