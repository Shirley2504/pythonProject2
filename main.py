import tkinter as tk
import random

# Clase para mostrar la ventana de verificar vocales
class VerificacionesDecorator:
    def __init__(self, funcion_original):
        self.funcion_original = funcion_original
        self.verificaciones = 1

    def __call__(self, *args, **kwargs):
        self.verificaciones += 1
        return self.funcion_original(*args, **kwargs)
verificador = VerificacionesDecorator(None)
cantidad_verificaciones = 0

def guardar_verificaciones(verificaciones):
    with open('verificaciones.txt', 'w') as file:
        file.write(str(verificaciones))

def leer_verificaciones():
    try:
        with open('verificaciones.txt', 'r') as file:
            verificaciones = int(file.read())
    except FileNotFoundError:
        verificaciones = 1
    return verificaciones


def mostrar_verificar_vocales():
    global verificador
    global cantidad_verificaciones

    ventana_verificar_vocales = tk.Toplevel()
    ventana_verificar_vocales.title("Verificar vocales")

    # Crear un label y una entrada para ingresar la letra
    label = tk.Label(ventana_verificar_vocales, text="Ingresa una letra:")
    label.pack()
    entrada = tk.Entry(ventana_verificar_vocales)
    entrada.pack()

    # Crear un botón para verificar si es vocal o no
    resultado = tk.Label(ventana_verificar_vocales, text="")
    resultado.pack()

    def es_vocal(letra):
        vocales = ["a", "e", "i", "o", "u"]
        if letra.lower() in vocales:
            return True
        else:
            return False

    @VerificacionesDecorator
    def verificar():
        global cantidad_verificaciones
        letra = entrada.get()
        if letra.isalpha() and len(letra) == 1:
            if es_vocal(letra):
                resultado.config(text="La letra es una vocal.")
            else:
                resultado.config(text="La letra no es una vocal.")
        else:
            resultado.config(text="Ingresa una letra válida.")
        cantidad_verificaciones = verificador.verificaciones
        resultado2.config(text=f"Se han realizado {verificador.verificaciones} verificaciones.")

    boton = tk.Button(ventana_verificar_vocales, text="Verificar", command=verificar)
    boton.pack()

    resultado2 = tk.Label(ventana_verificar_vocales, text="")
    resultado2.pack()

    verificador = VerificacionesDecorator(verificar)
    verificador.verificaciones = leer_verificaciones()


# Función para mostrar la ventana de contar palabras

class ContadorPalabras:
    _instance = None
    def __init__(self):
        pass


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._cantidad_palabras = 0
        return cls._instance

    def contar_palabras(self, texto):
        palabras = texto.split()
        self._cantidad_palabras = len(palabras)
        return self._cantidad_palabras



def ventanacontador():
    # Crear ventana
    # Crear instancia del contador de palabras
    contador = ContadorPalabras()

    def contar_palabras_click():
        texto = entrada_texto.get("1.0", tk.END)
        cantidad_palabras = contador.contar_palabras(texto)
        resultado.config(text="Cantidad de palabras: {}".format(cantidad_palabras))
    ventana = tk.Tk()
    ventana.title("Contador de palabras")

    # Crear entrada de texto
    entrada_texto = tk.Text(ventana, height=10, width=50)
    entrada_texto.pack()

    # Crear botón para contar palabras
    boton_contar = tk.Button(ventana, text="Contar palabras", command=contar_palabras_click)
    boton_contar.pack()

    # Crear etiqueta para mostrar el resultado
    resultado = tk.Label(ventana, text="")
    resultado.pack()



    # Ejecutar la ventana
    ventana.mainloop()

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



def salir():
    ventana_principal.destroy()


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("PRACTIQUEMOS JUNTOS ESPAÑOL")

# Crear botones para cada opción
boton_verificar_vocales = tk.Button(ventana_principal, text="Verificar vocales", command=mostrar_verificar_vocales)
boton_verificar_vocales.pack()

boton_contador_palabras = tk.Button(ventana_principal, text="Contador de palabras", command=ventanacontador)
boton_contador_palabras.pack()

boton_ordenador_palabras = tk.Button(ventana_principal, text="Ordenador de palabras", command=ordena_las_palabras)
boton_ordenador_palabras.pack()

boton_salir = tk.Button(ventana_principal, text="Salir", command=salir)
boton_salir.pack()

# Ejecutar la ventana principal
ventana_principal.mainloop()
