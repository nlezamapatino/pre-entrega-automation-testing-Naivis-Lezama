
import logging
import os
import pytest

os.makedirs("reports", exist_ok=True)

logger = logging.getLogger("pruebas")
logger.setLevel(logging.INFO)

archivo_log = logging.FileHandler(
    "reports/ejecucion.log",
    encoding="utf-8"
)

formato = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

archivo_log.setFormatter(formato)

if not logger.handlers:
    logger.addHandler(archivo_log)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call":
        if reporte.passed:
            logger.info("Prueba aprobada: %s", item.name)

        elif reporte.failed:
            logger.error("Prueba fallida: %s", item.name)

            navegador = item.funcargs.get("navegador")

            if navegador:
                nombre = item.name
                ruta = os.path.join(
                    "reports",
                    nombre + "_fallo.png"
                )

                navegador.save_screenshot(ruta)