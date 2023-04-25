# clase para mostrar la ventana de verificar vocales
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
