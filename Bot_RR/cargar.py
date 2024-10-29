# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout

# class FileLoaderApp(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # Crear un label y un botón para cargar el archivo
#         self.cargar_label = QLabel('No se ha seleccionado ningún archivo', self)
#         self.cargar_btn = QPushButton('Cargar archivo .xlsx', self)
#         self.cargar_btn.clicked.connect(self.cargar_archivo)

#         # Layout para organizar el label y el botón
#         layout = QVBoxLayout()
#         layout.addWidget(self.cargar_label)
#         layout.addWidget(self.cargar_btn)

#         self.setLayout(layout)}
#         self.setWindowTitle('Cargar archivo Excel')

#     def cargar_archivo(self):
#         # Abrir el diálogo de archivo y permitir seleccionar un archivo .xlsx
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
#         if file_name:
#             # Mostrar la ruta del archivo en el label
#             self.cargar_label.setText(f'Archivo seleccionado: {file_name}')


# if __name__ == '__main__':
#     app = QApplication([])
#     ventana = FileLoaderApp()
#     ventana.show()
#     app.exec_()




# import tkinter as tk
# from tkinter import simpledialog

# # Crear ventana raíz (oculta)
# root = tk.Tk()
# root.withdraw()  # Ocultar la ventana principal

# # Crear un cuadro de diálogo de entrada de texto
# input_value = simpledialog.askstring("Input", "Por favor, ingresa tu nombre:")

# # Mostrar el valor ingresado
# if input_value:
#     print(f"Has ingresado: {input_value}")





# import tkinter as tk
# from tkinter import simpledialog, messagebox

# # Función para mostrar un mensaje con un ícono de advertencia
# def show_warning_and_ask_input():
#     # Mostrar un mensaje con el ícono de advertencia
#     messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")
#     messagebox.showinfo("Información", "Este es un mensaje de información.")
#     messagebox.showerror("Error", "Este es un mensaje de error.")

#     result = messagebox.askquestion("Pregunta", "¿Quieres continuar?")
#     if result == 'yes':
#         print("El usuario seleccionó Sí.")
#     else:
#         print("El usuario seleccionó No.")

#     result = messagebox.askokcancel("Confirmar", "¿Seguro que quieres hacer esto?")
#     if result:
#         print("El usuario seleccionó Aceptar.")
#     else:
#         print("El usuario seleccionó Cancelar.")


#     result = messagebox.askyesno("Pregunta", "¿Estás seguro?")
#     if result:
#         print("El usuario seleccionó Sí.")
#     else:
#         print("El usuario seleccionó No.")


#     result = messagebox.askretrycancel("Error", "¿Quieres intentar de nuevo?")
#     if result:
#         print("El usuario seleccionó Reintentar.")
#     else:
#         print("El usuario seleccionó Cancelar.")



#     # Crear un cuadro de diálogo de entrada de texto
#     input_value = simpledialog.askstring("Input", "Ingresa tu nombre:")

#     # Mostrar el valor ingresado
#     if input_value:
#         print(f"Has ingresado: {input_value}")
#     else:
#         print("No se ha ingresado ningún nombre.")

# # Crear ventana raíz (oculta)
# root = tk.Tk()
# root.withdraw()  # Ocultar la ventana principal

# # Llamar a la función para mostrar el cuadro de diálogo
# show_warning_and_ask_input()

# # Cerrar la ventana raíz después de usar el cuadro de diálogo
# root.quit()

import autoit
import time

import sys
try:
    # Verifica si autoit está funcionando
    print("AutoIt version:", autoit.version)

    # Ejecuta Notepad
    autoit.run_program("notepad.exe")

except Exception as e:
    print(autoit.__version__) 
    print(autoit.__file__)  # Esto debe mostrar la ruta del archivo del módulo
    print(f"Error al ejecutar AutoIt: {e}", file=sys.stderr)
    time.sleep(5)



# Abre el Bloc de Notas (Notepad)
autoit.run("notepad.exe")

# Espera un poco para asegurarse de que se abra
time.sleep(2)

# Activa la ventana de Notepad (busca la ventana por título)
autoit.win_active("Untitled - Notepad")  # Para inglés
# Si el sistema está en español, podrías usar "Sin título - Bloc de notas"

# Escribe en la ventana de Notepad
autoit.send("Hola desde AutoIt en Python!")

# Espera para que puedas ver el resultado
time.sleep(2)

# Cierra Notepad, sin guardar
autoit.win_close("[CLASS:Notepad]") 
time.sleep(1)
title = autoit.win_get_title("[ACTIVE]")
print(f"El título actual de la ventana es: {title}")
autoit.control_click("[CLASS:#32770]", "Button2")  # Hace clic en 'No guardar' cuando aparece el cuadro de diálogo
