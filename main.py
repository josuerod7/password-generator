import tkinter as tk
import random
import string

# Función para generar una contraseña
def generar_contrasena_btn():
    longitud = int(entry_longitud.get())
    contrasena = generar_contrasena(longitud)
    texto_contrasena.delete("1.0", tk.END)  # Limpiar el widget Text
    texto_contrasena.insert(tk.END, contrasena)  # Insertar la contraseña generada

# Función para generar la contraseña
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Crear etiqueta y entrada para la longitud
lbl_longitud = tk.Label(ventana, text="Longitud:")
lbl_longitud.pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

# Crear botón para generar la contraseña
btn_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contrasena_btn)
btn_generar.pack()

# Crear widget Text para mostrar la contraseña generada
texto_contrasena = tk.Text(ventana, height=1, width=20)
texto_contrasena.pack()

# Habilitar la opción de copiar texto
def copiar_contrasena():
    contrasena = texto_contrasena.get("1.0", tk.END)
    ventana.clipboard_clear()
    ventana.clipboard_append(contrasena)
    ventana.update()  # Actualizar el portapapeles

btn_copiar = tk.Button(ventana, text="Copiar Contraseña", command=copiar_contrasena)
btn_copiar.pack()

# Iniciar el bucle de la aplicación
ventana.mainloop()