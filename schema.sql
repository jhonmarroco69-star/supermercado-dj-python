-- ============================================================
-- Base de datos: supermercado_dj
-- Ejecutar este script en MySQL Workbench o phpMyAdmin antes de
-- correr la aplicación.
-- ============================================================

CREATE DATABASE IF NOT EXISTS supermercado_dj;
USE supermercado_dj;

CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    codigo      VARCHAR(20)  NOT NULL UNIQUE,
    nombre      VARCHAR(100) NOT NULL,
    categoria   VARCHAR(50),
    stock       INT          NOT NULL DEFAULT 0,
    precio      DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    correo     VARCHAR(100),
    telefono   VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    cargo       VARCHAR(50),
    correo      VARCHAR(100),
    estado      ENUM('Activo', 'Inactivo') DEFAULT 'Activo'
);

-- Datos de ejemplo para probar la aplicación
INSERT INTO productos (codigo, nombre, categoria, stock, precio) VALUES
    ('P-001', 'Arroz Diana 500g', 'Abarrotes', 120, 3500),
    ('P-002', 'Leche Alpina 1L', 'Lácteos', 45, 4200);

INSERT INTO clientes (nombre, correo, telefono) VALUES
    ('Maria Torres', 'maria.torres@correo.com', '3001234567'),
    ('Carlos Perez', 'carlos.perez@correo.com', '3019876543');

INSERT INTO empleados (nombre, cargo, correo, estado) VALUES
    ('Laura Gomez', 'Cajera', 'laura.gomez@supermercadodj.com', 'Activo'),
    ('Andres Rios', 'Administrador', 'andres.rios@supermercadodj.com', 'Activo');
