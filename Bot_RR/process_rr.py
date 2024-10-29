import os
import time
import autoit
import clipboard
import pandas as pd
from PyQt5.QtWidgets import QMessageBox

class ControladorAs400():
    def __init__(self, obj_) -> None:
        # self.directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.troncales = []
        self.process = False
        self.CLASSAS400 = "[class:SunAwtFrame]"
        self.obj_ = obj_ 
        self.text = ''

        # self.Usuario = "C46118345"
        # self.Clave = "Paloma17**"

        # self.Usuario = "C46145004"
        # self.Clave = "Prueba28**"

        # self.Usuario = "C45049091"
        # self.Clave = "Jirafa78**"

        # self.Usuario = "C46221389"
        # self.Clave = "Cambio24**"

        # self.Usuario = "C46145004"
        # self.Clave = "Sanber24**"

    def get_control(self):        
        #handleApp = autoit.win_get_handle(CLASSAS400)
        #tituloApp = autoit.win_get_title_by_handle(handleApp)        
        activador = autoit.win_active(self.CLASSAS400)
        # autoit.win_wait_active(CLASSAS400, timeout=10)  # Esperar a que se active
        if activador == 0:            
            autoit.win_activate(self.CLASSAS400) 
            return True
        return False

    def EnviarComandosToPantalla(self, comandos, pantallaEsperada):
        for comando in comandos:
            autoit.send(comando)
            time.sleep(0.5)
        
        if pantallaEsperada in self.copiarPantalla():
            return True
        return False

    def Login(self):
        self.get_control()
        PantallActual = self.copiarPantalla()
        if "Inicio de Sesión" in PantallActual:
            # return self.EnviarComandosToPantalla([self.Usuario, "{TAB}", self.Clave, "{ENTER}"], "Información de inicio de sesión")
            return self.EnviarComandosToPantalla([self.obj_.user_input.text(), "{TAB}", self.obj_.pass_input.text(), "{ENTER}"], "Información de inicio de sesión")
	
    def EnviarComandosToPantalla(self,arraycomandos,titulo):
        self.get_control()
        '''se espera en u array las teclas pulsadas y tambien los datos a ingresar y valida la pantalla final'''        
        for i in arraycomandos:
            autoit.send(i)
            time.sleep(0.25)
        time.sleep(1)
        # text = clipboard.paste()    
        self.text = self.copiarPantalla()
        if titulo in self.text:
            return True
        else:
            return False
	
    def EnviarComandosToPantalla_Fast(self,arraycomandos,titulo,sTime=0.01):
        self.get_control()
        '''se espera en u array las teclas pulsadas y tambien los datos a ingresar y valida la pantalla final'''        
        for i in arraycomandos:
            autoit.send(i)
            time.sleep(sTime) # 0.01
        time.sleep(1)
        # text = clipboard.paste()    
        text = self.copiarPantalla()
        if titulo in text:
            return True
        else:
            return False

    def copiarPantalla(self):
        self.get_control()
        for i in ["^a","^c"]:
            autoit.send(i)
        # print(clipboard.paste())
        return clipboard.paste()

    def Xlogin(self):

        self.get_control()
        PantallActual = self.copiarPantalla()
        if not "Inicio de Sesión" in PantallActual:

            self.get_control()
            time.sleep(1)				
            autoit.send("+{ESC}")
            time.sleep(1)
            autoit.send("90")
            time.sleep(1)
            autoit.send("{ENTER}")
            self.Login()

    @classmethod
    def EstraerText(self):
        facturadoOK=False
        for row in range(1,7):			
            autoit.send("+{UP}")
            for i in range(1,17):
                autoit.send("+{LEFT}")					
            autoit.send("^c")			
            if "OP  UTP OPUTP" in clipboard.paste():				
                facturadoOK=True
                return facturadoOK
            else:
                autoit.send("{DOWN}")

    def SelectItem(self,items):
        for i in [items,"{DOWN}","{ENTER}","0","{DOWN}","{ENTER}","{ENTER}"]:
            autoit.send(i)
            time.sleep(1)
        autoit.send("{F2}")		
        return "Hay   1 compras en esta O/T." in self.copiarPantalla()

    def buscar(self):
        return self.EnviarComandosToPantalla(["{ENTER}","{ESC}","8","{ENTER}","7","{ENTER}","1","{ENTER}"],"Proceso de seleccion de nodos")     	

    def nodo(self, nodo):
        # return self.EnviarComandosToPantalla(["QB01A2","2","{ENTER}"],"Modificación de nodo")    
        print(nodo) 	
        return self.EnviarComandosToPantalla([nodo,"2","{ENTER}"],"Modificación de nodo")     	

    def actualizar_nodo(self):
        return self.EnviarComandosToPantalla_Fast(["{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","{TAB}","ACT","{ENTER}", "{F10}","{F3}"],"Proceso de seleccion de nodos")     	

    def actualizar_fecha(self, nodo, fecha):

        while True:
            if not self.EnviarComandosToPantalla_Fast(["{F3}","{F3}","{F3}","{F3}","{F3}","{F3}","{ESC}","1","{ENTER}","2","{ENTER}"],"Menu de Tablas Basicas Cuentas Matrices", 0.1): 
                continue

            if not self.EnviarComandosToPantalla_Fast(["80","{ENTER}","6","{ENTER}"],"MANTENIMIENTO INFORMACION NODO", 0.1):
                continue
        
            if not self.EnviarComandosToPantalla_Fast([nodo, "{ENTER}","{TAB}","2","{ENTER}"],"Fecha Apertura:", 0.1):
                continue

            if not self.EnviarComandosToPantalla_Fast([fecha.split(' ')[0],"{F2}","{F3}","{F3}","{F3}","{F3}","{F3}","{F3}"],"Menu Principal Sistema de Administracion Cable", 0.05):
                continue
            break
        return

    def read_excel(self):

        # Leer el archivo completo
        df = pd.read_excel(self.obj_.file_name)

        # Verificar si las columnas necesarias están presentes
        encabezado_requerido = ['ID DE TRONCAL', 'FECHA RECEPCIÓN']

        # Verificar si ambos encabezados están en las columnas del DataFrame
        if all(col in df.columns for col in encabezado_requerido):
            # Quitar los espacios de inicio y fin en la columna 'ID DE TRONCAL'
            df['TRONCAL'] = df['ID DE TRONCAL'].astype(str).str.strip()
            
            # Quitar los espacios de inicio y fin en la columna 'FECHA RECEPCIÓN'
            df['FECHA'] = df['FECHA RECEPCIÓN'].astype(str).str.replace('-', '/').str.strip()
            
            encabezado = ['TRONCAL', 'FECHA']
            self.troncales = df[encabezado]  # Solo mantener las columnas necesarias
            # print(df) 
            return True, ''
        else:
            faltantes = [col for col in encabezado_requerido if col not in df.columns]
            print(f"Error: Las siguientes columnas no se encontraron: {faltantes}")
            return False, f"Error: Las siguientes columnas no se encontraron: {faltantes}"

    def start_process(self):
        print('')

        success, data = self.read_excel()
        if not success:
            QMessageBox.warning(self.obj_, "Advertencia", data)
            return False

        if not self.get_control():
            QMessageBox.warning(self.obj_, "Advertencia", 'Verifica que RR este abierto correctamente.!')

        print(self.troncales)
 
        if self.Login():
            for n, (troncal, fecha) in enumerate(zip(self.troncales['TRONCAL'], self.troncales['FECHA']), start=2):
                if not self.buscar():
                    break
                os.system('cls' if os.name == 'nt' else 'clear')
                print(n,' de ', len(self.troncales))
                print(f'Índice: {n}, Troncal: {troncal}, Fecha: {fecha}')
                if self.nodo(troncal):
                    if self.actualizar_nodo():
                        self.actualizar_fecha(troncal, fecha)


            self.Xlogin()
            return True
        
        if self.process:
            exit()

        self.Xlogin()
        self.obj_.raise_()
        self.obj_.activateWindow() 
        
        try:
            print(self.text)
            QMessageBox.warning(self.obj_, "Advertencia", self.text.split('establecido')[1])
        except:
            QMessageBox.warning(self.obj_, "Advertencia", "Error en el proceso de Login")
            