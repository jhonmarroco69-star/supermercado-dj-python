"""Módulo 3 (interfaz gráfica): menú principal mostrado después de iniciar sesión."""

import tkinter as tk

from supermercado_dj.modelo.usuario import Usuario
from supermercado_dj.vista.ventana_productos import VentanaProductos
from supermercado_dj.vista.ventana_clientes import VentanaClientes
from supermercado_dj.vista.ventana_empleados import VentanaEmpleados


def construir_pantalla_principal(raiz: tk.Tk, usuario_activo: Usuario) -> None:
    """
    Construye el menú principal dentro de la ventana 'raiz'. Cada
    módulo (productos, clientes, empleados) se abre como una ventana
    secundaria independiente, de la misma forma que el módulo de
    agendamiento de citas se abre en el ejemplo de la clínica
    veterinaria.
    """
    raiz.title("Supermercado DJ - Menú principal")
    raiz.geometry("400x320")
    raiz.resizable(False, False)

    contenedor = tk.Frame(raiz, padx=20, pady=20)
    contenedor.pack(expand=True, fill="both")

    tk.Label(contenedor, text="Supermercado DJ", font=("Arial", 16, "bold")).pack(pady=(0, 5))
    tk.Label(
        contenedor,
        text=f"Sesión activa: {usuario_activo.nombre_usuario} ({usuario_activo.rol})",
        font=("Arial", 9),
    ).pack(pady=(0, 15))

    tk.Button(
        contenedor, text="Productos", width=25,
        command=lambda: VentanaProductos(raiz),
    ).pack(pady=5)

    tk.Button(
        contenedor, text="Clientes", width=25,
        command=lambda: VentanaClientes(raiz),
    ).pack(pady=5)

    tk.Button(
        contenedor, text="Empleados", width=25,
        command=lambda: VentanaEmpleados(raiz),
    ).pack(pady=5)

    tk.Button(
        contenedor, text="Cerrar sesión", width=25, fg="red",
        command=raiz.destroy,
    ).pack(pady=(20, 0))
