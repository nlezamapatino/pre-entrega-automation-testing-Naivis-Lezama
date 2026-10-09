import pytest
from selenium import webdriver

from utils.funciones_saucedemo import abrir_saucedemo, iniciar_sesion, validar_pagina_inventario, obtener_primer_producto, agregar_primer_producto, abrir_carrito, obtener_contador_carrito, obtener_nombre_producto_carrito, validar_menu_catalogo, validar_filtro_catalogo


@pytest.fixture
def navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador

    navegador.quit()


# Prueba para comprobar que el inicio de sesion
def test_login_exitoso(navegador):
    abrir_saucedemo(navegador)
    iniciar_sesion(navegador)
    validar_pagina_inventario(navegador)

    # Comprueba que el usuario fue redirigido al catalogo
    assert "/inventory.html" in navegador.current_url


# Comprobar que el catalogo muestra sus productos
def test_catalogo(navegador):
    """Verifica que exista al menos un producto visible en el catálogo."""

    abrir_saucedemo(navegador)
    iniciar_sesion(navegador)
    validar_menu_catalogo(navegador)
    validar_filtro_catalogo(navegador)

    nombre, precio = obtener_primer_producto(navegador)

    assert nombre
    assert precio


 # Con esta se quiere probar que se puede agregar un producto al carrito.   
def test_carrito(navegador):
    """Verifica que se pueda agregar un producto al carrito."""

    abrir_saucedemo(navegador)
    iniciar_sesion(navegador)

    nombre, precio = obtener_primer_producto(navegador)

    agregar_primer_producto(navegador)

    contador = obtener_contador_carrito(navegador)

    assert contador == "1"

    abrir_carrito(navegador)

    nombre_carrito = obtener_nombre_producto_carrito(navegador)

    assert nombre_carrito == nombre




