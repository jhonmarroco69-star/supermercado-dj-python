"""Módulo 4 (app): construye el flujo completo de la interfaz gráfica."""

import tkinter as tk

from supermercado_dj.modelo.usuario import Usuario
from supermercado_dj.vista.ventana_login import construir_pantalla_login
from supermercado_dj.vista.ventana_principal import construir_pantalla_principal


def iniciar_aplicacion() -> None:
    """
    Punto de entrada de la interfaz gráfica. Primero muestra la
    ventana de login; al iniciar sesión correctamente, destruye esa
    ventana y abre el menú principal en una ventana nueva.
    """
    raiz_login = tk.Tk()

    def al_iniciar_sesion(usuario_activo: Usuario) -> None:
        raiz_login.destroy()
        raiz_principal = tk.Tk()
        construir_pantalla_principal(raiz_principal, usuario_activo)
        raiz_principal.mainloop()

    construir_pantalla_login(raiz_login, al_iniciar_sesion)
    raiz_login.mainloop()
