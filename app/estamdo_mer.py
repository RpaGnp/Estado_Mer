import os
import time
from pathlib import Path
from platform import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import Select
from datetime import date

load_dotenv()
BASEDIR = Path('.').absolute()

class bot():

    def __init__(self):
        self.userMER = os.getenv('USER') 
        self.pswMER = os.getenv('PSW')

    def get_chrome_options(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        
        # Configurar las preferencias de descarga
        options.add_experimental_option("prefs", {
            "download.default_directory": '/home/seluser/Downloads',   # Directorio de descarga
            "download.prompt_for_download": False,  # No preguntar por la ubicación de descarga
            "download.directory_upgrade": True,  # Actualizar el directorio de descarga si cambia
            "safebrowsing.enabled": True,  # Habilitar la navegación segura
            "safebrowsing.disable_download_protection": True,  # Deshabilitar protección de descarga
            "profile.default_content_settings.popups": 0,  # Bloquear ventanas emergentes
            "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,  # Permitir descargas automáticas
            "profile.default_content_setting_values.automatic_downloads": 1,  # Permitir descargas múltiples
        })
        return options

    def create_browser(self):        

        if 'Windows' in platform():
            # print('The operating system is Windows\nWe will look for "Opera"')
            # from selenium.webdriver.opera.options import Options as OperaOptions

            # opera_options = OperaOptions()
            # opera_options.binary_location = r'%s\AppData\Local\Programs\Opera\opera.exe' % os.path.expanduser('~')
            # opera_options.add_argument('--start-maximized')
            # self.driver = webdriver.Opera(executable_path=r'C:\dchrome\operadriver.exe', options=opera_options)

            print('The operating system is Windows\nWe will look for "Chrome"')
            
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')  # Mantener otras opciones
            self.driver = webdriver.Chrome(executable_path=r'C:\dchrome\chromedriver.exe', options=chrome_options)

        else:
            time.sleep(10)
            chrome_options = self.get_chrome_options()
            chrome_host = os.getenv('CHROME_HOST', 'localhost')
            self.driver = webdriver.Remote(
                command_executor=f'http://{chrome_host}:4444/wd/hub',
                options=chrome_options
            )

    def login_wf(self):

        self.driver.get("https://mglapp.claro.com.co/catastro-warIns/view/MGL/template/login.xhtml?faces-redirect=true")
        self.wait = WebDriverWait(self.driver, 1)

        try:
            user_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'usuario')))
        except Exception as e:
            print('No encontro los campos de logueo')
            exit()
        print('Ingresando usuario')
        user_field.clear()
        user_field.send_keys(self.userMER)

        print('Ingresando password')
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="j_idt29"]/div/div/fieldset/div[3]/input')))
        password_field.clear()
        password_field.send_keys(self.pswMER)

        self.driver.find_element(by=By.XPATH, value='//*[@id="j_idt29"]/div/div/fieldset/div[5]/div/div').click()

        # Intenta encontrar el elemento 'messagesPop'
        if self.chek_object('messagesPop', 'La contraseña es errónea', 3):
            print('tienes que cambiar la contraseña')
            exit()

        # Intenta encontrar el elemento 'formPrincipal', imagen de claro
        if self.chek_object('formPrincipal', 'ingresó!', 60):
           self.process() 

    def process(self):
        
        menu_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'formPrincipal:menuVtGestionSolicitud'))
        )
        self.driver.execute_script("arguments[0].click();", menu_element)

        salir = False
        for i in range(1, 100):
            if salir:
                break
            for i in range(1, 11):
                
                filtro_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="formPrincipal:filtro"]'))
                )
                select = Select(filtro_element)
                select.select_by_value("2") 

                #valida que el filtro por CAMBIO ESTRETO este aplicado.
                while True:
                    cont = 0
                    for x in range(1, 11):
                        try:
                            tipo = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="formPrincipal:solicitudDthList"]/tbody/tr[{x}]/td[5]/div'))).text
                            if tipo == 'CAMBIO ESTRATO':
                                cont += 1
                        except:
                            pass
                    if cont == 10:
                        break

                print('')
                id = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="formPrincipal:solicitudDthList"]/tbody/tr[{i}]/td[3]'))).text
                dia = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="formPrincipal:solicitudDthList"]/tbody/tr[{i}]/td[4]'))).text.split()[0].split('-')[2]
                estado = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="formPrincipal:solicitudDthList"]/tbody/tr[{i}]/td[7]'))).text
                text_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="formPrincipal:solicitudDthList"]/tbody/tr[{i}]/td[1]/div/input'))).get_attribute('value')
                tipo = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="formPrincipal:solicitudDthList"]/tbody/tr[{i}]/td[5]/div'))).text

                if int(dia) != int(date.today().day):
                    salir = True
                    break

                if estado == 'PENDIENTE' and tipo == 'CAMBIO ESTRATO' and text_btn == 'Gestionar' and int(dia) == int(date.today().day):
                    print(id)
                    print(dia)
                    print(estado)
                    print(text_btn)
                    print(tipo)
                    print('actualizar')

                    menu_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.NAME , f'formPrincipal:solicitudDthList:{i-1}:j_idt332'))
                    )
                    self.driver.execute_script("arguments[0].click();", menu_element)

                    try:
                        btn_acept = WebDriverWait(self.driver, 3).until(
                            EC.element_to_be_clickable((By.ID, 'cerrarMensajeErrorBtn'))
                        )
                        btn_acept.click()
                        continue
                    except:
                        pass


                    try:
                        filtro_element = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="formSolicitud:resultadoRespuestaCamEst"]'))
                        )
                    
                    except:
                       
                        try:
                            btn_back = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located((By.ID, 'formSolicitud:gestionSolBack'))
                            )
                            self.driver.execute_script("arguments[0].click();", btn_back)
                            filtro_element = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="formPrincipal:filtro"]'))
                            )
                            select = Select(filtro_element)
                            select.select_by_value("2") 
                            continue

                        except:

                            try:
                                btn_back = WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.ID, 'formSolicitud:goBack'))
                                )
                                self.driver.execute_script("arguments[0].click();", btn_back)

                                filtro_element = WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="formPrincipal:filtro"]'))
                                )
                                select = Select(filtro_element)
                                select.select_by_value("2") 

                                continue
                            
                            except:

                                btn_back = WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="formSolicitud:goBackCamEst"]'))
                                )
                                self.driver.execute_script("arguments[0].click();", btn_back)

                                filtro_element = WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="formPrincipal:filtro"]'))
                                )
                                select = Select(filtro_element)
                                select.select_by_value("2") 

                                continue


                    select = Select(filtro_element)
                    select.select_by_value("GESTION DE HHPP DE FORMA MANUAL") 

                    btn_acept = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="formSolicitud:aceptarButtonCamEst"]'))
                    )
                    self.driver.execute_script("arguments[0].click();", btn_acept)

                    btn_acept = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.ID, 'cerrarMensajeErrorBtn'))
                    )
                    btn_acept.click()
                    btn_back = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="formSolicitud:goBackCamEst"]'))
                    )
                    self.driver.execute_script("arguments[0].click();", btn_back)

                    print('fecha.text')

            menu_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME , f'formPrincipal:solicitudDthList:j_idt387'))
                )
            self.driver.execute_script("arguments[0].click();", menu_element)

        print('no hay registros')
        self.close_all()

    def chek_object(self, obj, msg, time):
        try:
            # self.wait.until(EC.presence_of_element_located((By.ID, obj)))
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.ID, obj)))
            print(msg)
            return True
        except:
            return False
 
    def clear_console(self):
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para Linux y macOS
            os.system('clear')

    def close_all(self):
        self.driver.quit()

if __name__ == '__main__':
    print('iniciando bot')
    while True:
        try:
            b = bot()
            b.create_browser()
            b.login_wf()
        except Exception as e :
            print('error: ', e)
            if 'Windows' in platform():
                b.close_all()
            
