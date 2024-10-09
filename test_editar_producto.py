import unittest
from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import HtmlTestRunner
from editar_producto_page import EditarProductoPage
from error_producto_page import ErrorProductoPage
import os
import sys
import django
# Agregar la ruta del directorio del proyecto Django al PYTHONPATH
sys.path.append(r"D:\clase\proyectos\miproyecto")
# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miproyecto.settings')
# Inicializar Django
django.setup()
from producto.models import Producto



class EditarProductoTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        #cls.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver_options = Options()
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=driver_options)
        cls.driver.implicitly_wait(10)
        cls.url_base = "http://localhost:9000/productos"
        cls.EditarPage = EditarProductoPage(cls.driver)
        cls.ErrorPage = ErrorProductoPage(cls.driver)        
        Producto.objects.all().delete()
        nuevo_producto = Producto(codigo="00000011",nombre="Iphone",descripcion="celular alta gama",precio=499.00,cantidad_minima=3)
        nuevo_producto.save()
        cls.producto_inicial = Producto.objects.get(codigo="00000011")
        
    def setUp(self):
        self.EditarPage.abrir(f"{self.url_base}/editar/{self.producto_inicial.id}")        
    
    def test_editar_producto(self):
        try:
            pagina_editar=self.EditarPage
            pagina_error=self.ErrorPage            
            codigo_producto = "000001"    
            nombre_producto = "A"
            cantidad_producto = 1
            precio_producto = 399
            descripcion_producto = "Celu"
            pagina_editar.ingresar_codigo(codigo_producto)
            pagina_editar.ingresar_nombre(nombre_producto)
            pagina_editar.ingresar_descripcion(descripcion_producto)
            pagina_editar.ingresar_cantidad_minima(cantidad_producto)
            pagina_editar.ingresar_precio(precio_producto)
            pagina_editar.editar_producto()
            error_mensaje_codigo = pagina_error.recuperar_error_codigo()
            error_mensaje_nombre = pagina_error.recuperar_error_nombre()
            error_mensaje_descripcion = pagina_error.recuperar_error_descripcion()
            self.assertEqual(error_mensaje_codigo,"Codigo: El código debe tener exactamente 8 caracteres","el mensaje de error codigo no coincide")
            self.assertEqual(error_mensaje_nombre,"Nombre: El nombre debe tener entre 5 y 80 caracteres.","el mensaje de error nombre no coincide")
            self.assertEqual(error_mensaje_descripcion,"Descripción: La descripción debe tener entre 10 y 200 caracteres.","el mensaje de error descripcion no coincide")
            
            
        except Exception as e:
            self.fail(str(e))            
    
    @classmethod    
    def tearDownClass(cls):
        Producto.objects.all().delete() 
        
def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(EditarProductoTest))
    return suite

if __name__ == '__main__':
    # Crear un ejecutor de pruebas que ejecuta la suite y genera un reporte en HTML
    runner = HtmlTestRunner.HTMLTestRunner(
        output='reportes',  # Carpeta donde se guardará el reporte
        report_name='actualizar_producto',  # Nombre del archivo del reporte
        report_title='Error en Actualizar producto previamente creado usando Selenium',  # Titulo del reporte
        combine_reports=True,  # Combina todas las pruebas en un único reporte
        add_timestamp=True  # Agrega una marca de tiempo al reporte
    )
    # Ejecutar la suite
    runner.run(suite())