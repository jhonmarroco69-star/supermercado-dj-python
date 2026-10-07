"""Módulo 2 (acceso a datos): CRUD completo sobre la tabla 'productos'."""

from typing import List, Optional

from supermercado_dj.conexion.conexion_bd import obtener_conexion
from supermercado_dj.modelo.producto import Producto


class ProductoDAO:
    """
    Clase de acceso a datos (DAO) encargada de las cuatro operaciones
    CRUD (insertar, consultar, actualizar, eliminar) sobre la tabla
    'productos' de la base de datos.
    """

    def insertar(self, producto: Producto) -> int:
        """Inserta un nuevo producto y devuelve el id generado."""
        sql = """
            INSERT INTO productos (codigo, nombre, categoria, stock, precio)
            VALUES (%s, %s, %s, %s, %s)
        """
        parametros = (
            producto.codigo,
            producto.nombre,
            producto.categoria,
            producto.stock,
            producto.precio,
        )
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            conexion.commit()
            return cursor.lastrowid

    def listar_todos(self) -> List[Producto]:
        """Consulta y devuelve todos los productos registrados."""
        sql = """
            SELECT id_producto, codigo, nombre, categoria, stock, precio
            FROM productos
            ORDER BY nombre
        """
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [Producto(*fila) for fila in filas]

    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        """Consulta un producto específico por su id."""
        sql = """
            SELECT id_producto, codigo, nombre, categoria, stock, precio
            FROM productos
            WHERE id_producto = %s
        """
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_producto,))
            fila = cursor.fetchone()
            return Producto(*fila) if fila else None

    def actualizar(self, producto: Producto) -> None:
        """Actualiza los datos de un producto existente."""
        sql = """
            UPDATE productos
            SET codigo = %s, nombre = %s, categoria = %s, stock = %s, precio = %s
            WHERE id_producto = %s
        """
        parametros = (
            producto.codigo,
            producto.nombre,
            producto.categoria,
            producto.stock,
            producto.precio,
            producto.id_producto,
        )
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            conexion.commit()

    def eliminar(self, id_producto: int) -> None:
        """Elimina un producto de la base de datos según su id."""
        sql = "DELETE FROM productos WHERE id_producto = %s"
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_producto,))
            conexion.commit()
