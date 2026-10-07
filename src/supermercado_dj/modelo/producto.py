"""Módulo 1 (modelo): representa un producto del inventario."""

from dataclasses import dataclass


@dataclass
class Producto:
    """
    Representa un producto del supermercado.

    Atributos:
        id_producto: identificador autogenerado por la base de datos.
        codigo: código interno único del producto (ej. 'P-001').
        nombre: nombre comercial del producto.
        categoria: categoría a la que pertenece (ej. 'Abarrotes').
        stock: cantidad disponible en inventario.
        precio: precio unitario de venta.
    """

    id_producto: int
    codigo: str
    nombre: str
    categoria: str
    stock: int
    precio: float
