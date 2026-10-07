"""Módulo 1 (modelo): representa un cliente registrado."""

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Representa un cliente del supermercado.

    Atributos:
        id_cliente: identificador autogenerado por la base de datos.
        nombre: nombre completo del cliente.
        correo: correo electrónico de contacto.
        telefono: número de teléfono de contacto.
    """

    id_cliente: int
    nombre: str
    correo: str
    telefono: str
