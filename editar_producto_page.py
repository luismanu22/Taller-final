from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class EditarProductoPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    localizador_campo_codigo = (By.ID,"id_codigo")
    localizador_campo_nombre = (By.ID,"id_nombre")
    localizador_campo_descripcion = (By.ID,"id_descripcion")
    localizador_campo_cantidad_minima = (By.ID,"id_cantidad_minima")
    localizador_campo_precio = (By.ID,"id_precio")
    localizador_campo_editar_button = (By.ID,"btnEdit")    
    
    
    def abrir(self,url):
        self.driver.get(url)     
    
    def ingresar_codigo(self,codigo):        
        codigo_campo = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_codigo))
        codigo_campo.clear()
        codigo_campo.send_keys(codigo)
        
    def ingresar_nombre(self,nombre):        
        nombre_campo = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_nombre))
        nombre_campo.clear()
        nombre_campo.send_keys(nombre)
        
    def ingresar_descripcion(self,descripcion):        
        descripcion_campo = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_descripcion))
        descripcion_campo.clear()
        descripcion_campo.send_keys(descripcion)
        
    def ingresar_cantidad_minima(self,cantidad_minima):
        cantidad_minima_campo = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_cantidad_minima))
        cantidad_minima_campo.clear()
        cantidad_minima_campo.send_keys(cantidad_minima)
        
    def ingresar_precio(self,precio):
        precio_campo = self.wait.until(EC.element_to_be_clickable(self.localizador_campo_precio))
        precio_campo.clear()
        precio_campo.send_keys(precio)
        
    def editar_producto(self):
        self.wait.until(EC.element_to_be_clickable(self.localizador_campo_editar_button)).click()