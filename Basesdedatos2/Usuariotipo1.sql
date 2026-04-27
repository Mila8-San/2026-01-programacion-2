-- USUARIO 1 (SOLO LECTURA)

-- PASO 1: Crear el usuario
CREATE USER 'lector_grupo'@'localhost' IDENTIFIED BY 'password123';

-- PASO 2: Asignar SOLO permiso de lectura sobre la base de datos
GRANT SELECT ON biblioteca.* TO 'lector_grupo'@'localhost';

-- PASO 3: Aplicar cambios
FLUSH PRIVILEGES;

-- PASO 4: Verificar que el permiso fue asignado
SHOW GRANTS FOR 'lector_grupo'@'localhost';

-- AHORA CONECTARSE COMO lector_grupo y ejecutar estas pruebas:

--  ESTO SÍ FUNCIONA (SELECT permitido)
SELECT * FROM Books;
SELECT * FROM Users;
SELECT * FROM Loans;

--  ESTO FALLA (INSERT no permitido - mostrar el error en pantalla)
INSERT INTO Books (Title, Author, Genre, PublicationYear, AvailableCopies, CategoryID)
VALUES ('Libro de prueba', 'Autor Test', 'Fiction', 2024, 1, 1);

--  ESTO FALLA (UPDATE no permitido)
UPDATE Books SET AvailableCopies = 10 WHERE BookID = 1;

--  ESTO FALLA (DELETE no permitido)
DELETE FROM Books WHERE BookID = 1;