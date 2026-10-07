"""Módulo 2 (acceso a datos): CRUD completo sobre la tabla 'clientes'."""

from typing import List, Optional

from supermercado_dj.conexion.conexion_bd import obtener_conexion
from supermercado_dj.modelo.cliente import Cliente


class ClienteDAO:
    """
    Clase de acceso a datos (DAO) encargada de las cuatro operaciones
    CRUD sobre la tabla 'clientes' de la base de datos.
    """

    def insertar(self, cliente: Cliente) -> int:
        """Inserta un nuevo cliente y devuelve el id generado."""
        sql = """
            INSERT INTO clientes (nombre, correo, telefono)
            VALUES (%s, %s, %s)
        """
        parametros = (cliente.nombre, cliente.correo, cliente.telefono)
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            conexion.commit()
            return cursor.lastrowid

    def listar_todos(self) -> List[Cliente]:
        """Consulta y devuelve todos los clientes registrados."""
        sql = "SELECT id_cliente, nombre, correo, telefono FROM clientes ORDER BY nombre"
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [Cliente(*fila) for fila in filas]

    def buscar_por_id(self, id_cliente: int) -> Optional[Cliente]:
        """Consulta un cliente específico por su id."""
        sql = "SELECT id_cliente, nombre, correo, telefono FROM clientes WHERE id_cliente = %s"
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_cliente,))
            fila = cursor.fetchone()
            return Cliente(*fila) if fila else None

    def actualizar(self, cliente: Cliente) -> None:
        """Actualiza los datos de un cliente existente."""
        sql = """
            UPDATE clientes
            SET nombre = %s, correo = %s, telefono = %s
            WHERE id_cliente = %s
        """
        parametros = (cliente.nombre, cliente.correo, cliente.telefono, cliente.id_cliente)
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            conexion.commit()

    def eliminar(self, id_cliente: int) -> None:
        """Elimina un cliente de la base de datos según su id."""
        sql = "DELETE FROM clientes WHERE id_cliente = %s"
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_cliente,))
            conexion.commit()
