"""Módulo 2 (acceso a datos): CRUD completo sobre la tabla 'empleados'."""

from typing import List, Optional

from supermercado_dj.conexion.conexion_bd import obtener_conexion
from supermercado_dj.modelo.empleado import Empleado


class EmpleadoDAO:
    """
    Clase de acceso a datos (DAO) encargada de las cuatro operaciones
    CRUD sobre la tabla 'empleados' de la base de datos.
    """

    def insertar(self, empleado: Empleado) -> int:
        """Inserta un nuevo empleado y devuelve el id generado."""
        sql = """
            INSERT INTO empleados (nombre, cargo, correo, estado)
            VALUES (%s, %s, %s, %s)
        """
        parametros = (empleado.nombre, empleado.cargo, empleado.correo, empleado.estado)
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            conexion.commit()
            return cursor.lastrowid

    def listar_todos(self) -> List[Empleado]:
        """Consulta y devuelve todos los empleados registrados."""
        sql = """
            SELECT id_empleado, nombre, cargo, correo, estado
            FROM empleados
            ORDER BY nombre
        """
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [Empleado(*fila) for fila in filas]

    def buscar_por_id(self, id_empleado: int) -> Optional[Empleado]:
        """Consulta un empleado específico por su id."""
        sql = """
            SELECT id_empleado, nombre, cargo, correo, estado
            FROM empleados
            WHERE id_empleado = %s
        """
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_empleado,))
            fila = cursor.fetchone()
            return Empleado(*fila) if fila else None

    def actualizar(self, empleado: Empleado) -> None:
        """Actualiza los datos de un empleado existente."""
        sql = """
            UPDATE empleados
            SET nombre = %s, cargo = %s, correo = %s, estado = %s
            WHERE id_empleado = %s
        """
        parametros = (
            empleado.nombre,
            empleado.cargo,
            empleado.correo,
            empleado.estado,
            empleado.id_empleado,
        )
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            conexion.commit()

    def eliminar(self, id_empleado: int) -> None:
        """Elimina un empleado de la base de datos según su id."""
        sql = "DELETE FROM empleados WHERE id_empleado = %s"
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_empleado,))
            conexion.commit()
