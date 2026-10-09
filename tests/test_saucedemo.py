import pytest
from selenium import webdriver

from utils.funciones_saucedemo import abrir_saucedemo, iniciar_sesion, validar_pagina_inventario, obtener_primer_producto, agregar_primer_producto, abrir_carrito, obtener_contador_carrito, obtener_nombre_producto_carrito, validar_menu_catalogo, validar_filtro_catalogo


@pytest.fixture
def navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador

    navegador.quit()


def test_login_exitoso(navegador):
    abrir_saucedemo(navegador)
    iniciar_sesion(navegador)
    validar_pagina_inventario(navegador)

    assert "/inventory.html" in navegador.current_url


def test_catalogo(navegador):
    """Verifica que exista al menos un producto visible en el catálogo."""

    abrir_saucedemo(navegador)
    iniciar_sesion(navegador)
    validar_menu_catalogo(navegador)
    validar_filtro_catalogo(navegador)

    nombre, precio = obtener_primer_producto(navegador)

    assert nombre
    assert precio
    
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




