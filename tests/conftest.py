import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("navegador")

        if navegador:
            os.makedirs("reports", exist_ok=True)

            nombre = item.name
            ruta = os.path.join("reports", nombre + "_fallo.png")

            navegador.save_screenshot(ruta)