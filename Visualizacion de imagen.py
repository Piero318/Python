import cv2 

imagen= cv2.imread("naruto.jpg") #nombre de la imagen guardada 
cv2.imshow("Prueba de visualizacion 1",imagen) #titulo del recuadro de la imagen
#cv2.imwrite("grises.jpg",imagen) #comando para guardar imagen
cv2.waitKey(1000) #tiempo de visualizacion de la imagen
cv2.destroyAllWindows()