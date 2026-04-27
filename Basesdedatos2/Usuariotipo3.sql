--USUARIO 3 (ADMINISTRADOR)

-- PASO 1: Crear el usuario
CREATE USER 'admin_grupo'@'localhost' IDENTIFIED BY 'password789';

-- PASO 2: Asignar TODOS los permisos sobre la base de datos
GRANT ALL PRIVILEGES ON biblioteca.* TO 'admin_grupo'@'localhost';

-- PASO 3: Aplicar cambios
FLUSH PRIVILEGES;

-- PASO 4: Verificar que tiene todos los permisos
SHOW GRANTS FOR 'admin_grupo'@'localhost';

-- AHORA CONECTARSE COMO admin_grupo y ejecutar estas pruebas:

-- PASO A: Crear una nueva tabla
CREATE TABLE EventosEspeciales (
    EventoID INT AUTO_INCREMENT PRIMARY KEY,
    NombreEvento VARCHAR(100) NOT NULL,
    FechaEvento DATE NOT NULL,
    Descripcion TEXT
);

-- PASO B: Insertar datos en la tabla creada
INSERT INTO EventosEspeciales (NombreEvento, FechaEvento, Descripcion)
VALUES 
('Feria del libro', '2024-11-15', 'Evento anual de presentación de nuevos títulos'),
('Club de lectura', '2024-11-22', 'Reunión mensual del club de lectura infantil');

-- Verificar que los datos quedaron guardados
SELECT * FROM EventosEspeciales;

-- PASO C: Eliminar la tabla (demostrar control total)
DROP TABLE EventosEspeciales;

-- Verificar que la tabla ya no existe
SHOW TABLES;