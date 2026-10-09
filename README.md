# Pre-entrega de Automation Testing

Este proyecto es una práctica de automatización de pruebas realizada con Python, Selenium y Pytest para el sitio web SauceDemo.

## Herramientas utilizadas

* Python
* Selenium
* Pytest
* Google Chrome
* Git y GitHub

## Pruebas realizadas

Se automatizaron las siguientes pruebas:

* Inicio de sesión con un usuario válido.
* Verificación del catálogo de productos.
* Agregado de un producto al carrito y comprobación de su contenido.

## Archivos del proyecto

* `tests/`: contiene los casos de prueba.
* `utils/`: contiene las funciones utilizadas en las pruebas.
* `reports/`: guarda el reporte HTML y las capturas de pantalla cuando ocurre un fallo.
* `requirements.txt`: contiene las librerías necesarias para ejecutar el proyecto.
* `conftest.py`: configura las capturas de pantalla cuando una prueba falla.

## Instalación

Instalar las dependencias con el siguiente comando:

```powershell
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Para ejecutar las pruebas desde la terminal:

```powershell
python -m pytest tests/test_saucedemo.py -v
```

Para generar el reporte HTML:

```powershell
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

## Usuario de prueba

* Usuario: `standard_user`
* Contraseña: `secret_sauce`
