"""Módulo 1 (modelo): representa un empleado del supermercado."""

from dataclasses import dataclass


@dataclass
class Empleado:
    """
    Representa un empleado del supermercado.

    Atributos:
        id_empleado: identificador autogenerado por la base de datos.
        nombre: nombre completo del empleado.
        cargo: cargo que desempeña (ej. 'Cajera', 'Administrador').
        correo: correo electrónico corporativo.
        estado: estado laboral ('Activo' o 'Inactivo').
    """

    id_empleado: int
    nombre: str
    cargo: str
    correo: str
    estado: str
