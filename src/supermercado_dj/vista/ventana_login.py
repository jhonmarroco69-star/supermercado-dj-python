"""Módulo 3 (interfaz gráfica): inicio de sesión."""

import tkinter as tk
from tkinter import ttk
from typing import Callable

from supermercado_dj.modelo.usuario import Usuario

# Usuario de prueba, mientras se conecta la tabla 'usuarios' de la BD.
USUARIO_DEMO = "admin"
CLAVE_DEMO = "admin"


def construir_pantalla_login(raiz: tk.Tk, al_iniciar_sesion: Callable[[Usuario], None]) -> None:
    """
    Construye la pantalla de inicio de sesión dentro de la ventana 'raiz'.
    Al validar las credenciales correctamente, llama a la función
    'al_iniciar_sesion' pasándole el Usuario que inició sesión.
    """
    raiz.title("Supermercado DJ - Inicio de sesión")
    raiz.geometry("360x240")
    raiz.resizable(False, False)

    contenedor = tk.Frame(raiz, padx=20, pady=20)
    contenedor.pack(expand=True, fill="both")

    tk.Label(contenedor, text="Supermercado DJ", font=("Arial", 16, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(0, 15)
    )

    tk.Label(contenedor, text="Usuario:").grid(row=1, column=0, sticky="w", pady=5)
    entrada_usuario = tk.Entry(contenedor, width=25)
    entrada_usuario.grid(row=1, column=1, pady=5)

    tk.Label(contenedor, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=5)
    entrada_contrasena = tk.Entry(contenedor, width=25, show="*")
    entrada_contrasena.grid(row=2, column=1, pady=5)

    etiqueta_mensaje = tk.Label(contenedor, text="", fg="red", wraplength=300)
    etiqueta_mensaje.grid(row=3, column=0, columnspan=2, pady=5)

    def validar_login() -> None:
        nombre_usuario = entrada_usuario.get().strip()
        contrasena = entrada_contrasena.get().strip()

        if not nombre_usuario or not contrasena:
            etiqueta_mensaje.config(text="Ingresa usuario y contraseña.")
            return

        if nombre_usuario == USUARIO_DEMO and contrasena == CLAVE_DEMO:
            usuario_activo = Usuario(nombre_usuario=nombre_usuario, rol="ADMINISTRADOR")
            al_iniciar_sesion(usuario_activo)
        else:
            etiqueta_mensaje.config(text="Usuario o contraseña incorrectos.")

    ttk.Button(contenedor, text="Iniciar sesión", command=validar_login).grid(
        row=4, column=0, columnspan=2, pady=(10, 0)
    )
