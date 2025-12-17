from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from process_rr import ControladorAs400

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.RR = ControladorAs400(self)

        # Configurar la ventana
        self.setWindowTitle('Troncales')
        self.setFixedSize(250, 300)  # Establecer dimensiones fijas

        # Calcular la posición para centrar la ventana
        screen = QApplication.primaryScreen()  # Obtener la pantalla principal
        screen_geometry = screen.geometry()    # Obtener la geometría de la pantalla
        x = (screen_geometry.width() - self.width()) // 2  # Calcular posición X
        y = (screen_geometry.height() - self.height()) // 2  # Calcular posición Y

        self.setGeometry(x, y, 250, 300)  # Establecer geometría centrada


        # Crear el layout
        layout = QVBoxLayout()

        # self.Usuario = "C46118345"
        # self.Clave = "Paloma17**"

        # self.Usuario = "C46145004"
        # self.Clave = "Prueba28**"

        # self.Usuario = "C45049091"
        # self.Clave = "Jirafa78**"

        # self.Usuario = "C46221389"
        # self.Clave = "Cambio24**"

        # C45528145
        # Julian12**

        # Campos de texto para credenciales
        self.user_label = QLabel('Usuario:')
        self.user_input = QLineEdit(self)
        self.user_input.setText("C46179873")

        self.pass_label = QLabel('Contraseña:')
        self.pass_input = QLineEdit(self)
        self.pass_input.setText("Estado30**")
        # Estado30**
        # Agregar botón para cargar archivo .xlsx
        self.cargar_archivo_label = QLabel('No se ha seleccionado ningún archivo .xlsx')
        self.cargar_archivo_button = QPushButton('Cargar archivo', self)
        self.cargar_archivo_button.clicked.connect(self.cargar_archivo)

        # Inicializar QLabel de la imagen del CAPTCHA
        self.image_label = QLabel('credenciales RR')
        self.image_label.setAlignment(Qt.AlignCenter)

        # QLabel para mostrar mensajes de error
        self.show_messege = QLabel('hola')
        self.show_messege.setStyleSheet('color: red;')  # Establecer el color del texto a rojo
        self.show_messege.hide()

        # Botón de envío
        self.send_button = QPushButton('Iniciar', self)
        self.send_button.hide()
        self.send_button.clicked.connect(self.RR.start_process)

        # Añadir widgets al layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.cargar_archivo_label)  # Mostrar la ruta del archivo seleccionado
        layout.addWidget(self.cargar_archivo_button)  # Botón para seleccionar archivo
        layout.addWidget(self.show_messege)
        layout.addWidget(self.send_button)

        # Configurar el layout
        self.setLayout(layout)

    def start_process(self):
        print('inicio')

    def cargar_archivo(self):
        # Abrir cuadro de diálogo para seleccionar archivo .xlsx
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if self.file_name and self.file_name.endswith('.xlsx'):
            # Si el archivo es un .xlsx, actualiza el QLabel
            self.cargar_archivo_label.setText(f'Archivo seleccionado: {self.file_name}')
            self.send_button.show()
            return True

        self.send_button.hide()
        self.raise_()
        self.activateWindow() 
        # QMessageBox.warning(self, "Formato no válido", "El archivo seleccionado no es un archivo Excel (.xlsx).")
        QMessageBox.warning(self, "Formato no válido", "El archivo seleccionado no es un archivo Excel (.xlsx).")
        return False

if __name__ == '__main__':
    app = QApplication([])
    ventana = ImageWindow()
    ventana.show()
    app.exec_()

