"""
Script de arranque rápido.

En vez de escribir en la terminal:
    cd src
    python -m supermercado_dj.app.aplicacion_principal

Simplemente abre ESTE archivo en VS Code y dale clic al botón ▶ (Run)
que aparece arriba a la derecha del editor, o presiona F5.
"""

import sys
from pathlib import Path

# Agrega la carpeta 'src' al path de Python, para que encuentre el paquete
# 'supermercado_dj' sin importar desde qué carpeta se ejecute este archivo.
CARPETA_SRC = Path(__file__).parent / "src"
sys.path.insert(0, str(CARPETA_SRC))

from supermercado_dj.app.aplicacion_principal_gui import iniciar_aplicacion

if __name__ == "__main__":
    iniciar_aplicacion()
