import tkinter as tk
import random


#ORDENADOR DE PALABRAS
def ordena_las_palabras():
    # Palabras a utilizar
    palabras = ["manzana", "perro", "lápiz", "computadora", "automóvil", "bicicleta", "libro", "televisor", "helado", "guitarra"]

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Ordena las Palabras")

    # Crear una matriz y un vector con las palabras
    matriz_palabras = []
    vector_palabras = []
    for palabra in palabras:
        # Agregar la palabra a la matriz
        matriz_palabras.append(list(palabra))

        # Desordenar la palabra y agregarla al vector
        lista_letras = list(palabra)
        random.shuffle(lista_letras)
        vector_palabras.append("".join(lista_letras))

    # Función para verificar si las palabras están en el orden correcto
    def verificar_orden():
        # Obtener las palabras ingresadas por el usuario
        palabras_ingresadas = []
        for i in range(len(palabras)):
            palabras_ingresadas.append(casillas_palabras[i].get())

        # Verificar si las palabras están en el orden correcto
        orden_correcto = True
        for i in range(len(palabras)):
            if palabras_ingresadas[i] != palabras[i]:
                orden_correcto = False

        # Mostrar un mensaje en la interfaz según si el orden es correcto o no
        if orden_correcto:
            mensaje.config(text="¡Muy bien! Las palabras están en el orden correcto.")
        else:
            mensaje.config(text="Lo siento, el orden de las palabras no es correcto. ¡Sigue intentando!")

    # Crear las casillas para ingresar las palabras
    casillas_palabras = []
    for i in range(len(palabras)):
        # Crear una etiqueta con la palabra desordenada
        palabra_desordenada = tk.Label(ventana, text=vector_palabras[i])
        palabra_desordenada.grid(row=i, column=0)

        # Crear una casilla para ingresar la palabra en el orden correcto
        casilla = tk.Entry(ventana)
        casilla.grid(row=i, column=1)
        casillas_palabras.append(casilla)

    # Crear un botón para verificar si las palabras están en el orden correcto
    boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_orden)
    boton_verificar.grid(row=len(palabras), column=0, columnspan=2)

    # Crear una etiqueta para mostrar el resultado
    mensaje = tk.Label(ventana, text="")
    mensaje.grid(row=len(palabras)+1, column=0, columnspan=2)

    # Devolver la ventana y ejecutar el mainloop()
    return ventana, ventana.mainloop()

