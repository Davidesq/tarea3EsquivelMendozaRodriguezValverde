# Se importan los modulos necesarios
import argparse
import os
import time
from prettytable import PrettyTable

# Se declara el parser
parser = argparse.ArgumentParser(description="Tabula cada palabra escrita en un archivo de texto y la cantidad de veces que se aparece.")

# Se declara el argumento que se va a trabajar con su descripción
parser.add_argument("archivo", type=str, help="Especifica el nombre del archivo de texto que se desea leer.")
parser.add_argument("--time", action='store_true', help='Cronometra el tiempo de ejecución')

# Se añaden al objeto args
args = parser.parse_args()

"""
Se declara el método print_Tabla con argumentos Archivo.
El argumento Archivo es un string con la ruta al archivo mp3 por reproducir,
mientras que Loops da la cantidad de veces que se quiere reproducir el audio.
"""


def print_Tabla(archivo):

    ti = time.time()  # Se define el inicio del conteo del tiempo

    fp = open(archivo, "r")  # Abre archivo de texto para lectura
    # Se lee líneas y se agrega cada palabra a una lista
    words = [word.strip() for line in fp.readlines() for word in line.split('_') if word.strip()]
    words_cont = len(words)

    # Se crea nuevo archivo para escribir tabla
    t = PrettyTable(['Palabra', 'Cantidad'])
    words_rep = open("x.txt", "w+")

    # Ciclo que compara la palabra de índice i con todas las demás palabras (índice n)
    i = 0
    while i < words_cont:
        n = 0
        cont = 0
        while n < words_cont:
            if words[i] == words[n]:
                cont = cont + 1
            n = n + 1
            if n == words_cont:  # Si ya se comparó con todas las demás palabras
                t.add_row([words[i], cont])  # Se agrega fila a la tabla
                i = i + 1  # Se pasa a la siguiente palabra que será comparada con todas las demás

    # Se escribe tabla en arhivo de texto
    words_rep.write(str(t))
    words_rep.close()


# NOTA: Cada vez que se repite una palabra se crea una nueva columna en la tabla.
# Por lo tanto, la siguiente porción de código elimina columnas repetidas

    lines_seen = set()  # Se retiene líneas leídas

    # Se crea nuevo archivo de texto donde se guardará la tabla sin columnas repetidas
    outfile = open("Tarea3_rep.txt", "w+")
    f = open("x.txt", "r")
    header = f.readlines()[0:3]

    for line in header:  # Para cada línea del header, se escribe en nuevo archivo de texto
        outfile.write(line)
    f.close()

    # Se lee las demás líneas donde sí se desea eliminar filas repetidas
    z = open("x.txt", "r")
    lines_post_header = z.readlines()[3:]
    for line in lines_post_header:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    z.close()

    outfile.close()  # Se cierra el archivo con la tabla correcta
    os.remove("x.txt")  # Se elimina el archivo de texto con la tabla con filas duplicadas

    tf = time.time()  # Fin del conteo de tiempo

    if args.time:
        print('-----------------------------------------------------------------------')
        print('FIN... Tiempo de ejecución en segundos: '+str(tf-ti))
    else:
        print('-----------------------------------------------------------------------')
        print('FIN...')

def mostrar_tabla(): #funcion que envuelve el metodo principal
    # Se llama la función con los argumentos pasados desde el parser
    print_Tabla(args.archivo)

if __name__=='__main__': #condicion para que se ejecute la funcion predeterminadamente
    mostrar_tabla()