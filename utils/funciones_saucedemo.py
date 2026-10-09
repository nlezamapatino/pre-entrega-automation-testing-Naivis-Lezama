from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def abrir_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")


def iniciar_sesion(driver):
    espera = WebDriverWait(driver, 10)

    usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    usuario.send_keys("standard_user")

    contrasena = driver.find_element(By.ID, "password")
    contrasena.send_keys("secret_sauce")

    boton = driver.find_element(By.ID, "login-button")
    boton.click()

    espera.until(EC.url_contains("/inventory.html"))


def obtener_primer_producto(driver):
    espera = WebDriverWait(driver, 10)

    producto = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    nombre = producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio = producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    return nombre, precio


def agregar_primer_producto(driver):
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".inventory_item button")
        )
    )
    boton.click()


def abrir_carrito(driver):
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()


def validar_pagina_inventario(driver):
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"
    assert "Swag Labs" in driver.title


def obtener_contador_carrito(driver):
    contador = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )
    return contador.text


def obtener_nombre_producto_carrito(driver):
    producto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )
    return producto.text


def validar_menu_catalogo(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()


def validar_filtro_catalogo(driver):
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()

