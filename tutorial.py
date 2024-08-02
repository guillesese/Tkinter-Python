import tkinter

ventana = tkinter.Tk()

# Dar dimensión a la ventana
ventana.geometry("300x300")

# Crear etiquetas.
etiqueta = tkinter.Label(ventana, text="Hola Mundo", bg="blue")
etiqueta.pack(side=tkinter.BOTTOM) # Agregar etiqueta a la ventana con posicionamiento
etiqueta.pack(fill=tkinter.X)      # Agregar etiqueta a la ventana con relleno completo.

# Crear botones

# Método para el funcionamiento del botón
def saludo(nombre):
    print("Hola "+nombre)

boton1 = tkinter.Button(ventana, text="Click", command= lambda: saludo("python"))
boton1.pack()

# Crear cajas de texto
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

## Función que recoge el valor de la caja y lo imprime en pantalla.
def textoCaja():
    texto = cajaTexto.get()
    etiqueta["text"] = texto

boton2 = tkinter.Button(ventana,text="Click2",command=textoCaja)
boton2.pack()


ventana.mainloop()