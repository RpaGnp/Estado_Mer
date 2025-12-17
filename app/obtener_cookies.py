from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.opera.options import Options as OperaOptions
import time
import os

def extraer_cookie_permisos(driver):
    """
    Extrae y retorna la cookie de permisos del navegador
    """
    try:
        # Obtener todas las cookies
        cookies = driver.get_cookies()
        
        # Buscar la cookie de permisos
        cookie_permisos = None
        for cookie in cookies:
            if 'permiso' in cookie['name'].lower() or 'permission' in cookie['name'].lower():
                cookie_permisos = cookie
                break
        
        if cookie_permisos:
            print("\n--- Cookie de Permisos ---")
            print("Nombre: {}".format(cookie_permisos['name']))
            print("Valor: {}".format(cookie_permisos['value']))
            print("Dominio: {}".format(cookie_permisos['domain']))
            print("Path: {}".format(cookie_permisos['path']))
            print("Timestamp: {}".format(time.strftime('%Y-%m-%d %H:%M:%S')))
            print("-" * 50)
            return cookie_permisos
        else:
            # Si no encuentra cookie específica, mostrar todas
            print("\n--- Todas las Cookies ---")
            for cookie in cookies:
                valor_truncado = cookie['value'][:50] if len(cookie['value']) > 50 else cookie['value']
                print("Nombre: {}, Valor: {}...".format(cookie['name'], valor_truncado))
            print("-" * 50)
            return cookies
            
    except Exception as e:
        print("Error al extraer cookies: {}".format(e))
        return None

def main():
    # Configurar opciones del navegador Opera
    opera_options = OperaOptions()
    opera_options.binary_location = r'%s\AppData\Local\Programs\Opera\opera.exe' % os.path.expanduser('~')
    opera_options.add_argument('--start-maximized')
    opera_options.add_argument('--disable-blink-features=AutomationControlled')
    try:
        driver = webdriver.Opera(executable_path=r'C:\dchrome\operadriver.exe', options=opera_options)
        wait = WebDriverWait(driver, 10)
    except Exception as e:
        print("Error al inicializar Opera: {}".format(e))
        print("\nAsegúrate de:")
        print("1. Tener OperaDriver en C:\\dchrome\\operadriver.exe")
        print("2. Tener Opera instalado en la ubicación por defecto")
        print("3. Que las versiones de Opera y OperaDriver sean compatibles")
        return
    
    try:
        print("Accediendo al sitio...")
        driver.get("https://moduloagenda.cable.net.co/")
        
        # Esperar y llenar el campo de usuario
        print("Ingresando usuario...")
        campo_usuario = wait.until(
            EC.presence_of_element_located((By.XPATH, 
                "/html/body/div[1]/div/div/div/div/div/form/div/div[3]/center/table/tbody/tr[2]/td[2]/input"))
        )
        campo_usuario.clear()
        campo_usuario.send_keys("46352857")
        
        # Esperar y llenar el campo de contraseña
        print("Ingresando contraseña...")
        campo_password = wait.until(
            EC.presence_of_element_located((By.XPATH,
                "/html/body/div[1]/div/div/div/div/div/form/div/div[3]/center/table/tbody/tr[3]/td[2]/input"))
        )
        campo_password.clear()
        campo_password.send_keys("DiI8iu7.*4")
        
        # Hacer clic en el botón de ingresar
        print("Haciendo clic en Ingresar...")
        boton_ingresar = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                "/html/body/div[1]/div/div/div/div/div/form/div/div[3]/center/table/tbody/tr[5]/td[2]/input[1]"))
        )
        boton_ingresar.click()
        
        # Esperar a que cargue la página
        time.sleep(2)
        
        # Hacer clic en el menú
        print("Haciendo clic en Menú...")
        menu = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/a"))
        )
        menu.click()
        
        time.sleep(1)
        
        # Hacer clic en Aprovisionamiento
        print("Haciendo clic en Aprovisionamiento...")
        aprovisionamiento = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/ul/li[3]/a"))
        )
        aprovisionamiento.click()
        
        time.sleep(1)
        
        # Hacer clic en Ingresar
        print("Haciendo clic en Ingresar (submenú)...")
        ingresar_submenu = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/ul/li[3]/ul/li[3]/a"))
        )
        ingresar_submenu.click()
        
        print("\n¡Navegación completada exitosamente!")
        time.sleep(2)
        
        # Extraer cookie inicialmente
        print("\nExtrayendo cookie de permisos...")
        extraer_cookie_permisos(driver)
        
        # Bucle para extraer la cookie constantemente
        print("\nMonitoreando cookies (presiona Ctrl+C para detener)...")
        try:
            while True:
                time.sleep(5)  # Esperar 5 segundos entre cada extracción
                extraer_cookie_permisos(driver)
        except KeyboardInterrupt:
            print("\n\nMonitoreo detenido por el usuario.")
        
    except TimeoutException:
        print("Error: Tiempo de espera agotado al buscar un elemento.")
    except Exception as e:
        print("Error durante la ejecución: {}".format(e))
    finally:
        print("\nCerrando el navegador...")
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    main()