# Se importan los modulos necesarios
import argparse
import time
from playsound import playsound

# Se declara el parser
parser = argparse.ArgumentParser(description='Reproduce un archivo de audio mp3 con la cantidad de loops que el usuario desee')

# Se declaran los argumentos que se van a trabajar con su descripción
parser.add_argument('Archivo', type=str, help='Especifica el archivo por reproducir')
parser.add_argument('Loops', type=int, help='Determina la cantidad de veces que se escuchará el audio')
parser.add_argument("--time", action='store_true', help='Cronometra el tiempo de ejecución')

# Se añaden al objeto args
args = parser.parse_args()

"""
Se declara el método reproducir_audio con argumentos Archivo y Loops.
El argumento Archivo es un string con la ruta al archivo mp3 por reproducir,
mientras que Loops da la cantidad de veces que se quiere reproducir el audio.
"""


def reproducir_audio(Archivo, Loops):

    ti = time.time()  # Se define el inicio del conteo del tiempo

    for i in range(Loops):  # Se repetirá la reproducción Loops veces
        print('-----------------------------------------------------------------------')
        print('AHORA: Reproduciendo la vuelta número... '+str(i+1))
        playsound(Archivo)  # Método de playsound que reproduce el audio

    tf = time.time()  # Fin del conteo de tiempo

    if args.time:
        print('-----------------------------------------------------------------------')
        print('FIN... Tiempo de ejecución en segundos: '+str(tf-ti))
    else:
        print('-----------------------------------------------------------------------')
        print('FIN...')


def play_audio(): #funcion que envuelve el metodo principal
    # Se llama la función con los argumentos pasados desde el parser
    reproducir_audio(args.Archivo, args.Loops)

if __name__=='__main__': #condicion para que se ejecute la funcion predeterminadamente
    play_audio()