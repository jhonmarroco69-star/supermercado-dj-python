"""
Módulo de utilidad encargado de abrir la conexión hacia la base de datos
"supermercado_dj" usando la librería 'mysql-connector-python' (el
conector oficial de MySQL para Python).

Instalación de la librería:
    pip install mysql-connector-python
"""

from contextlib import contextmanager
from typing import Iterator

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract

# Estándar de nombramiento: constantes en MAYÚSCULAS_CON_GUION_BAJO.
HOST_BD = "localhost"
PUERTO_BD = 3307
NOMBRE_BD = "supermercado_dj"
USUARIO_BD = "root"
CLAVE_BD = "MiClave123"


@contextmanager
def obtener_conexion() -> Iterator[MySQLConnectionAbstract]:
    """
    Abre una conexión hacia la base de datos y la libera (cierra)
    automáticamente al salir del bloque 'with', incluso si ocurre
    un error durante su uso.

    Uso típico dentro de un DAO:

        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            ...
    """
    conexion = mysql.connector.connect(
        host=HOST_BD,
        port=PUERTO_BD,
        database=NOMBRE_BD,
        user=USUARIO_BD,
        password=CLAVE_BD,
    )
    try:
        yield conexion
    finally:
        conexion.close()
        