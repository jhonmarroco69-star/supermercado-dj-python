"""Módulo 1 (modelo): representa un usuario que inicia sesión en el sistema."""

from dataclasses import dataclass


@dataclass
class Usuario:
    """
    Representa al usuario que ha iniciado sesión en la aplicación.

    Atributos:
        nombre_usuario: nombre o correo con el que inició sesión.
        rol: rol dentro del sistema (ej. 'ADMINISTRADOR', 'CAJERO').
    """

    nombre_usuario: str
    rol: str
