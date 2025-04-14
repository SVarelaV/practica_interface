from tkinter import *


#funciones de procesamiento
def procesar():
	miEdad = str(2025-int(anio_nacimiento.get()))
	print(f"Hola {nombre.get()}, tu edad es: {miEdad} años.")


#Instancia de la clase Tk
ventana = Tk()
ventana.title('SALUDOS')

#Variables que almacenarán los datos
nombre = StringVar()
anio_nacimiento = IntVar()


#generación de widgets
#peso
etiqueta_nombre = Label(ventana, text='Nombre:')
entrada_nombre = Entry(ventana, textvariable=nombre)
etiqueta_nombre.grid(row=1, column=1)
entrada_nombre.grid(row=1, column=2)


#año de nacimiento
etiqueta_anio_nacimiento = Label(ventana, text='Año de Nacimiento: ')
entrada_anio_nacimiento = Entry(ventana, textvariable=anio_nacimiento)
etiqueta_anio_nacimiento.grid(row=2, column=1)
entrada_anio_nacimiento.grid(row=2, column=2)


#boton
boton = Button(ventana, text='Calcular edad', command=procesar, width=10)
boton.grid(row=4, column=2)

#ejecución de ventana
ventana.mainloop()