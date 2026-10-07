# Supermercado DJ - Módulo de codificación (Python + MySQL)

Aplicación de escritorio (Tkinter) con conexión a base de datos MySQL,
desarrollada para la evidencia **GA7-220501096-AA2-EV01: Codificación
de módulos del software**.

## Arquitectura

El proyecto sigue el patrón **MVC + DAO**, organizado en paquetes:

```
src/supermercado_dj/
├── app/        → arranque de la aplicación
├── conexion/   → conexión centralizada a la base de datos
├── dao/        → clases *DAO con el CRUD de cada entidad
├── modelo/     → clases que representan cada entidad
└── vista/      → ventanas de la interfaz gráfica (Tkinter)
```

## Estándares de codificación aplicados

| Elemento | Convención | Ejemplo |
|---|---|---|
| Clases | PascalCase | `ProductoDAO`, `VentanaProductos` |
| Funciones y variables | snake_case | `obtener_conexion`, `entrada_nombre` |
| Constantes | MAYÚSCULAS_CON_GUION_BAJO | `HOST_BD`, `PUERTO_BD` |
| Paquetes y archivos | minúsculas_con_guion_bajo | `conexion_bd.py`, `producto_dao.py` |

## Requisitos

- Python 3.10 o superior
- MySQL Server (o XAMPP)

## Instalación

```bash
pip install -r requirements.txt
```

## Configuración de la base de datos

1. Ejecuta el script `schema.sql` en MySQL Workbench o phpMyAdmin.
2. Si tu usuario/contraseña de MySQL son distintos a `root`/`root`,
   ajústalos en `src/supermercado_dj/conexion/conexion_bd.py`.

## Ejecución

Desde la carpeta `src`:

```bash
cd src
python -m supermercado_dj.app.aplicacion_principal
```

Usuario de prueba para el login: `admin` / `admin`.

## Funcionalidades CRUD implementadas

- **Productos**: insertar, consultar, actualizar y eliminar.
- **Clientes**: insertar, consultar, actualizar y eliminar.
- **Empleados**: insertar, consultar, actualizar y eliminar.
