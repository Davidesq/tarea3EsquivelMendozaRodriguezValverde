# Se importan los modulos necesarios
import cv2
import argparse
import time

# Se declara el parser
parser = argparse.ArgumentParser(description='Muestra una imagen en la escala seleccionada.')

# Se declararn los argumentos que se van a trabajar con su descripción
parser.add_argument('Ruta', type=str, help='Especifica la ruta de la imagen')
parser.add_argument('Escala', type=int, help='Seleccione la escala: 0 -> 1:1, 1 -> 2:1, 2 -> 1:2')
parser.add_argument("--time", action='store_true', help='Cronometra el tiempo de ejecución')

# Se añaden al objeto args
args = parser.parse_args()

"""
Se declara el método print_imagen con argumentos Ruta y tipo.
El argumento Ruta es un string con la ruta a la imagen por mostrar,
mientras que tipo es la escala en la cual se mostrará la imagen
"""


def print_imagen(Ruta, tipo):
    image = cv2.imread(Ruta)  # Se abre la imagen en la ruta especificada
    ancho = image.shape[1]  # Se extrae el ancho de la imagen
    alto = image.shape[0]  # Se extrae el alto de la imagen
    # Se hace un condicional para los casos de escalado

    ti = time.time()  # Se define el inicio del conteo del tiempo

    print('-----------------------------------------------------------------------')
    print('Presione cualquier tecla para cerrar la imagen...')

    if tipo == 0:  # Caso 0 escala 1:1
        imageOut = cv2.resize(image, (1*ancho, 1*alto), interpolation=cv2.INTER_CUBIC)  # Se edita la imagen para la escala dada
        cv2.imshow('Imagen final', imageOut)  # Se muestra la imagen ya escalada
        cv2.waitKey(0)  # Se espera a cualquier tecla para continuar
        cv2.destroyAllWindows()  # Cuando se presiona la tecla se cierran la ventana

    # Esto se repite para cada caso
    if tipo == 1:
        imageOut = cv2.resize(image, (2*ancho, 2*alto), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('Imagen final', imageOut)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if tipo == 2:
        imageOut = cv2.resize(image, (int(0.5*ancho), int(0.5*alto)), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('Imagen final', imageOut)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    tf = time.time()  # Fin del conteo del tiempo

    if args.time:
        print('-----------------------------------------------------------------------')
        print('FIN... Tiempo de ejecución en segundos: '+str(tf-ti))
    else:
        print('-----------------------------------------------------------------------')
        print('FIN...')

def mostrar_imagen(): #funcion que envuelve el metodo principal
    # Se llama la función con los argumentos pasados desde el parser
    print_imagen(args.Ruta, args.Escala)

if __name__=='__main__': #condicion para que se ejecute la funcion predeterminadamente
    mostrar_imagen()