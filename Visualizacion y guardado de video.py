import cv2 

captura= cv2.VideoCapture("videosalida_de_prueba_1.avi")
#salida= cv2.VideoWriter("videosalida_de_prueba_1.avi",cv2.VideoWriter_fourcc(*"XVID"), 20.0,(640,480)) #comando para guardar video


while (captura.isOpened()):
	ret,imagen=captura.read() #ret es un argumento booleano (T O F)
	if ret==True:
		cv2.imShow("Video",imagen)
		salida.write(imagen)
		if cv2.waitKey(30) & 0XFF == ord("s"): # S para cerrar la ventana de video, "30" el tiempo de procesamiento de video 
			break 
    else :break

captura.release()
#salida.release() parte del comando para guardar videos
cv2.destroyAllWindows()