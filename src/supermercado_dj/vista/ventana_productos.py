"""Módulo 3 (interfaz gráfica): gestión de productos, con CRUD completo."""

import tkinter as tk
from tkinter import messagebox, ttk

from supermercado_dj.dao.producto_dao import ProductoDAO
from supermercado_dj.modelo.producto import Producto


class VentanaProductos(tk.Toplevel):
    """
    Ventana del módulo de productos. Implementa las cuatro operaciones
    CRUD (insertar, consultar, actualizar, eliminar) sobre la tabla
    'productos', apoyándose en ProductoDAO.
    """

    def __init__(self, padre: tk.Misc):
        super().__init__(padre)
        self.title("Productos")
        self.geometry("520x420")

        self.producto_dao = ProductoDAO()
        self.id_seleccionado: int | None = None

        self._construir_formulario()
        self._construir_tabla()
        self._construir_botones()
        self.cargar_productos()

    def _construir_formulario(self) -> None:
        contenedor = tk.Frame(self, padx=15, pady=15)
        contenedor.pack(fill="x")

        tk.Label(contenedor, text="Código:").grid(row=0, column=0, sticky="w", pady=3)
        self.entrada_codigo = tk.Entry(contenedor, width=30)
        self.entrada_codigo.grid(row=0, column=1, pady=3)

        tk.Label(contenedor, text="Nombre:").grid(row=1, column=0, sticky="w", pady=3)
        self.entrada_nombre = tk.Entry(contenedor, width=30)
        self.entrada_nombre.grid(row=1, column=1, pady=3)

        tk.Label(contenedor, text="Categoría:").grid(row=2, column=0, sticky="w", pady=3)
        self.entrada_categoria = tk.Entry(contenedor, width=30)
        self.entrada_categoria.grid(row=2, column=1, pady=3)

        tk.Label(contenedor, text="Stock:").grid(row=3, column=0, sticky="w", pady=3)
        self.entrada_stock = tk.Entry(contenedor, width=30)
        self.entrada_stock.grid(row=3, column=1, pady=3)

        tk.Label(contenedor, text="Precio:").grid(row=4, column=0, sticky="w", pady=3)
        self.entrada_precio = tk.Entry(contenedor, width=30)
        self.entrada_precio.grid(row=4, column=1, pady=3)

    def _construir_tabla(self) -> None:
        columnas = ("id", "codigo", "nombre", "categoria", "stock", "precio")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)
        for columna, titulo in zip(
            columnas, ("ID", "Código", "Nombre", "Categoría", "Stock", "Precio")
        ):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=80)
        self.tabla.pack(fill="both", expand=True, padx=15)
        self.tabla.bind("<<TreeviewSelect>>", self._al_seleccionar_fila)

    def _construir_botones(self) -> None:
        barra = tk.Frame(self, pady=10)
        barra.pack()

        tk.Button(barra, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=5)
        tk.Button(barra, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=1, padx=5)
        tk.Button(barra, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        tk.Button(barra, text="Limpiar formulario", command=self.limpiar_formulario).grid(row=0, column=3, padx=5)

    def cargar_productos(self) -> None:
        """Consulta todos los productos y refresca la tabla (operación: Consultar)."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.producto_dao.listar_todos():
            self.tabla.insert(
                "", "end",
                values=(producto.id_producto, producto.codigo, producto.nombre,
                        producto.categoria, producto.stock, producto.precio),
            )

    def agregar_producto(self) -> None:
        """Inserta un nuevo producto (operación: Insertar)."""
        try:
            producto = Producto(
                id_producto=0,
                codigo=self.entrada_codigo.get().strip(),
                nombre=self.entrada_nombre.get().strip(),
                categoria=self.entrada_categoria.get().strip(),
                stock=int(self.entrada_stock.get().strip()),
                precio=float(self.entrada_precio.get().strip()),
            )
        except ValueError:
            messagebox.showerror("Datos inválidos", "Stock y precio deben ser numéricos.")
            return

        if not producto.codigo or not producto.nombre:
            messagebox.showerror("Datos incompletos", "Código y nombre son obligatorios.")
            return

        self.producto_dao.insertar(producto)
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        self.limpiar_formulario()
        self.cargar_productos()

    def actualizar_producto(self) -> None:
        """Actualiza el producto seleccionado en la tabla (operación: Actualizar)."""
        if self.id_seleccionado is None:
            messagebox.showwarning("Selecciona un producto", "Elige un producto de la tabla primero.")
            return

        try:
            producto = Producto(
                id_producto=self.id_seleccionado,
                codigo=self.entrada_codigo.get().strip(),
                nombre=self.entrada_nombre.get().strip(),
                categoria=self.entrada_categoria.get().strip(),
                stock=int(self.entrada_stock.get().strip()),
                precio=float(self.entrada_precio.get().strip()),
            )
        except ValueError:
            messagebox.showerror("Datos inválidos", "Stock y precio deben ser numéricos.")
            return

        self.producto_dao.actualizar(producto)
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        self.limpiar_formulario()
        self.cargar_productos()

    def eliminar_producto(self) -> None:
        """Elimina el producto seleccionado en la tabla (operación: Eliminar)."""
        if self.id_seleccionado is None:
            messagebox.showwarning("Selecciona un producto", "Elige un producto de la tabla primero.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar el producto seleccionado?")
        if confirmar:
            self.producto_dao.eliminar(self.id_seleccionado)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.limpiar_formulario()
            self.cargar_productos()

    def limpiar_formulario(self) -> None:
        self.id_seleccionado = None
        for entrada in (self.entrada_codigo, self.entrada_nombre,
                         self.entrada_categoria, self.entrada_stock, self.entrada_precio):
            entrada.delete(0, tk.END)

    def _al_seleccionar_fila(self, _evento: tk.Event) -> None:
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")
        self.id_seleccionado = int(valores[0])

        self.limpiar_campos_sin_perder_id()
        self.entrada_codigo.insert(0, valores[1])
        self.entrada_nombre.insert(0, valores[2])
        self.entrada_categoria.insert(0, valores[3])
        self.entrada_stock.insert(0, valores[4])
        self.entrada_precio.insert(0, valores[5])

    def limpiar_campos_sin_perder_id(self) -> None:
        for entrada in (self.entrada_codigo, self.entrada_nombre,
                         self.entrada_categoria, self.entrada_stock, self.entrada_precio):
            entrada.delete(0, tk.END)
