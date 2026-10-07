"""Módulo 3 (interfaz gráfica): gestión de clientes, con CRUD completo."""

import tkinter as tk
from tkinter import messagebox, ttk

from supermercado_dj.dao.cliente_dao import ClienteDAO
from supermercado_dj.modelo.cliente import Cliente


class VentanaClientes(tk.Toplevel):
    """
    Ventana del módulo de clientes. Implementa las cuatro operaciones
    CRUD (insertar, consultar, actualizar, eliminar) sobre la tabla
    'clientes', apoyándose en ClienteDAO.
    """

    def __init__(self, padre: tk.Misc):
        super().__init__(padre)
        self.title("Clientes")
        self.geometry("480x400")

        self.cliente_dao = ClienteDAO()
        self.id_seleccionado: int | None = None

        self._construir_formulario()
        self._construir_tabla()
        self._construir_botones()
        self.cargar_clientes()

    def _construir_formulario(self) -> None:
        contenedor = tk.Frame(self, padx=15, pady=15)
        contenedor.pack(fill="x")

        tk.Label(contenedor, text="Nombre:").grid(row=0, column=0, sticky="w", pady=3)
        self.entrada_nombre = tk.Entry(contenedor, width=30)
        self.entrada_nombre.grid(row=0, column=1, pady=3)

        tk.Label(contenedor, text="Correo:").grid(row=1, column=0, sticky="w", pady=3)
        self.entrada_correo = tk.Entry(contenedor, width=30)
        self.entrada_correo.grid(row=1, column=1, pady=3)

        tk.Label(contenedor, text="Teléfono:").grid(row=2, column=0, sticky="w", pady=3)
        self.entrada_telefono = tk.Entry(contenedor, width=30)
        self.entrada_telefono.grid(row=2, column=1, pady=3)

    def _construir_tabla(self) -> None:
        columnas = ("id", "nombre", "correo", "telefono")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)
        for columna, titulo in zip(columnas, ("ID", "Nombre", "Correo", "Teléfono")):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=100)
        self.tabla.pack(fill="both", expand=True, padx=15)
        self.tabla.bind("<<TreeviewSelect>>", self._al_seleccionar_fila)

    def _construir_botones(self) -> None:
        barra = tk.Frame(self, pady=10)
        barra.pack()

        tk.Button(barra, text="Agregar", command=self.agregar_cliente).grid(row=0, column=0, padx=5)
        tk.Button(barra, text="Actualizar", command=self.actualizar_cliente).grid(row=0, column=1, padx=5)
        tk.Button(barra, text="Eliminar", command=self.eliminar_cliente).grid(row=0, column=2, padx=5)
        tk.Button(barra, text="Limpiar formulario", command=self.limpiar_formulario).grid(row=0, column=3, padx=5)

    def cargar_clientes(self) -> None:
        """Consulta todos los clientes y refresca la tabla (operación: Consultar)."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for cliente in self.cliente_dao.listar_todos():
            self.tabla.insert(
                "", "end",
                values=(cliente.id_cliente, cliente.nombre, cliente.correo, cliente.telefono),
            )

    def agregar_cliente(self) -> None:
        """Inserta un nuevo cliente (operación: Insertar)."""
        cliente = Cliente(
            id_cliente=0,
            nombre=self.entrada_nombre.get().strip(),
            correo=self.entrada_correo.get().strip(),
            telefono=self.entrada_telefono.get().strip(),
        )

        if not cliente.nombre:
            messagebox.showerror("Datos incompletos", "El nombre es obligatorio.")
            return

        self.cliente_dao.insertar(cliente)
        messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
        self.limpiar_formulario()
        self.cargar_clientes()

    def actualizar_cliente(self) -> None:
        """Actualiza el cliente seleccionado en la tabla (operación: Actualizar)."""
        if self.id_seleccionado is None:
            messagebox.showwarning("Selecciona un cliente", "Elige un cliente de la tabla primero.")
            return

        cliente = Cliente(
            id_cliente=self.id_seleccionado,
            nombre=self.entrada_nombre.get().strip(),
            correo=self.entrada_correo.get().strip(),
            telefono=self.entrada_telefono.get().strip(),
        )
        self.cliente_dao.actualizar(cliente)
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
        self.limpiar_formulario()
        self.cargar_clientes()

    def eliminar_cliente(self) -> None:
        """Elimina el cliente seleccionado en la tabla (operación: Eliminar)."""
        if self.id_seleccionado is None:
            messagebox.showwarning("Selecciona un cliente", "Elige un cliente de la tabla primero.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar el cliente seleccionado?")
        if confirmar:
            self.cliente_dao.eliminar(self.id_seleccionado)
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            self.limpiar_formulario()
            self.cargar_clientes()

    def limpiar_formulario(self) -> None:
        self.id_seleccionado = None
        for entrada in (self.entrada_nombre, self.entrada_correo, self.entrada_telefono):
            entrada.delete(0, tk.END)

    def _al_seleccionar_fila(self, _evento: tk.Event) -> None:
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")
        self.id_seleccionado = int(valores[0])

        for entrada in (self.entrada_nombre, self.entrada_correo, self.entrada_telefono):
            entrada.delete(0, tk.END)
        self.entrada_nombre.insert(0, valores[1])
        self.entrada_correo.insert(0, valores[2])
        self.entrada_telefono.insert(0, valores[3])
