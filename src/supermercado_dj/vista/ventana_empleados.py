"""Módulo 3 (interfaz gráfica): gestión de empleados, con CRUD completo."""

import tkinter as tk
from tkinter import messagebox, ttk

from supermercado_dj.dao.empleado_dao import EmpleadoDAO
from supermercado_dj.modelo.empleado import Empleado


class VentanaEmpleados(tk.Toplevel):
    """
    Ventana del módulo de empleados. Implementa las cuatro operaciones
    CRUD (insertar, consultar, actualizar, eliminar) sobre la tabla
    'empleados', apoyándose en EmpleadoDAO.
    """

    def __init__(self, padre: tk.Misc):
        super().__init__(padre)
        self.title("Empleados")
        self.geometry("520x400")

        self.empleado_dao = EmpleadoDAO()
        self.id_seleccionado: int | None = None

        self._construir_formulario()
        self._construir_tabla()
        self._construir_botones()
        self.cargar_empleados()

    def _construir_formulario(self) -> None:
        contenedor = tk.Frame(self, padx=15, pady=15)
        contenedor.pack(fill="x")

        tk.Label(contenedor, text="Nombre:").grid(row=0, column=0, sticky="w", pady=3)
        self.entrada_nombre = tk.Entry(contenedor, width=30)
        self.entrada_nombre.grid(row=0, column=1, pady=3)

        tk.Label(contenedor, text="Cargo:").grid(row=1, column=0, sticky="w", pady=3)
        self.entrada_cargo = tk.Entry(contenedor, width=30)
        self.entrada_cargo.grid(row=1, column=1, pady=3)

        tk.Label(contenedor, text="Correo:").grid(row=2, column=0, sticky="w", pady=3)
        self.entrada_correo = tk.Entry(contenedor, width=30)
        self.entrada_correo.grid(row=2, column=1, pady=3)

        tk.Label(contenedor, text="Estado:").grid(row=3, column=0, sticky="w", pady=3)
        self.combo_estado = ttk.Combobox(contenedor, values=["Activo", "Inactivo"], width=27, state="readonly")
        self.combo_estado.grid(row=3, column=1, pady=3)
        self.combo_estado.set("Activo")

    def _construir_tabla(self) -> None:
        columnas = ("id", "nombre", "cargo", "correo", "estado")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)
        for columna, titulo in zip(columnas, ("ID", "Nombre", "Cargo", "Correo", "Estado")):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=90)
        self.tabla.pack(fill="both", expand=True, padx=15)
        self.tabla.bind("<<TreeviewSelect>>", self._al_seleccionar_fila)

    def _construir_botones(self) -> None:
        barra = tk.Frame(self, pady=10)
        barra.pack()

        tk.Button(barra, text="Agregar", command=self.agregar_empleado).grid(row=0, column=0, padx=5)
        tk.Button(barra, text="Actualizar", command=self.actualizar_empleado).grid(row=0, column=1, padx=5)
        tk.Button(barra, text="Eliminar", command=self.eliminar_empleado).grid(row=0, column=2, padx=5)
        tk.Button(barra, text="Limpiar formulario", command=self.limpiar_formulario).grid(row=0, column=3, padx=5)

    def cargar_empleados(self) -> None:
        """Consulta todos los empleados y refresca la tabla (operación: Consultar)."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for empleado in self.empleado_dao.listar_todos():
            self.tabla.insert(
                "", "end",
                values=(empleado.id_empleado, empleado.nombre, empleado.cargo,
                        empleado.correo, empleado.estado),
            )

    def agregar_empleado(self) -> None:
        """Inserta un nuevo empleado (operación: Insertar)."""
        empleado = Empleado(
            id_empleado=0,
            nombre=self.entrada_nombre.get().strip(),
            cargo=self.entrada_cargo.get().strip(),
            correo=self.entrada_correo.get().strip(),
            estado=self.combo_estado.get(),
        )

        if not empleado.nombre:
            messagebox.showerror("Datos incompletos", "El nombre es obligatorio.")
            return

        self.empleado_dao.insertar(empleado)
        messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
        self.limpiar_formulario()
        self.cargar_empleados()

    def actualizar_empleado(self) -> None:
        """Actualiza el empleado seleccionado en la tabla (operación: Actualizar)."""
        if self.id_seleccionado is None:
            messagebox.showwarning("Selecciona un empleado", "Elige un empleado de la tabla primero.")
            return

        empleado = Empleado(
            id_empleado=self.id_seleccionado,
            nombre=self.entrada_nombre.get().strip(),
            cargo=self.entrada_cargo.get().strip(),
            correo=self.entrada_correo.get().strip(),
            estado=self.combo_estado.get(),
        )
        self.empleado_dao.actualizar(empleado)
        messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
        self.limpiar_formulario()
        self.cargar_empleados()

    def eliminar_empleado(self) -> None:
        """Elimina el empleado seleccionado en la tabla (operación: Eliminar)."""
        if self.id_seleccionado is None:
            messagebox.showwarning("Selecciona un empleado", "Elige un empleado de la tabla primero.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar el empleado seleccionado?")
        if confirmar:
            self.empleado_dao.eliminar(self.id_seleccionado)
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            self.limpiar_formulario()
            self.cargar_empleados()

    def limpiar_formulario(self) -> None:
        self.id_seleccionado = None
        for entrada in (self.entrada_nombre, self.entrada_cargo, self.entrada_correo):
            entrada.delete(0, tk.END)
        self.combo_estado.set("Activo")

    def _al_seleccionar_fila(self, _evento: tk.Event) -> None:
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")
        self.id_seleccionado = int(valores[0])

        for entrada in (self.entrada_nombre, self.entrada_cargo, self.entrada_correo):
            entrada.delete(0, tk.END)
        self.entrada_nombre.insert(0, valores[1])
        self.entrada_cargo.insert(0, valores[2])
        self.entrada_correo.insert(0, valores[3])
        self.combo_estado.set(valores[4])
