# Función para mostrar la ventana de contar palabras
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
