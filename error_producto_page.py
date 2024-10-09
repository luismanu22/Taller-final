from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ErrorProductoPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    localizador_error_codigo = (By.XPATH,"/html/body/div/div[1]/section[2]/div/div/div/div/div[2]/span")   
    localizador_error_nombre = (By.XPATH,"/html/body/div/div[1]/section[2]/div/div/div/div/div[2]/span[2]")   
    localizador_error_descripcion = (By.XPATH,"/html/body/div/div[1]/section[2]/div/div/div/div/div[2]/span[3]")   
    
    def abrir(self,url):
        self.driver.get(url)     
    
    def recuperar_error_codigo(self):        
        campo_codigo_error = self.wait.until(EC.visibility_of_element_located(self.localizador_error_codigo))
        return campo_codigo_error.text
        
    def recuperar_error_nombre(self):        
        campo_nombre_error = self.wait.until(EC.visibility_of_element_located(self.localizador_error_nombre))
        return campo_nombre_error.text
        
    def recuperar_error_descripcion(self):        
        campo_descripcion_error = self.wait.until(EC.visibility_of_element_located(self.localizador_error_descripcion))
        return campo_descripcion_error.text