-- 1. Obtener los nombres y apellidos de los usuarios que han reservado un libro de la categoría "Fiction".
SELECT FirstName, LastName
FROM Users
WHERE UserID IN (
    SELECT UserID
    FROM Reservations
    WHERE BookID IN (
        SELECT BookID
        FROM Books
        WHERE CategoryID = (
            SELECT CategoryID
            FROM BookCategories
            WHERE CategoryName = 'Fiction'
        )
    )
);

-- 2. Mostrar el título y autor de los libros que están prestados.
SELECT Title, Author
FROM Books
WHERE BookID IN (
    SELECT BookID
    FROM Loans
    WHERE ReturnDate IS NULL
);

-- 3. Encontrar los títulos de los libros que han sido reservados, pero no prestados.
SELECT B.Title
FROM Books B
JOIN Reservations R ON B.BookID = R.BookID
EXCEPT
SELECT B.Title
FROM Books B
JOIN Loans L ON B.BookID = L.BookID;

-- 4. Encontrar los títulos de los libros que han sido prestados, pero no reservados.
SELECT B.Title
FROM Books B
JOIN Loans L ON B.BookID = L.BookID
EXCEPT
SELECT B.Title
FROM Books B
JOIN Reservations R ON B.BookID = R.BookID;

-- 5. Mostrar un listado de todos los libros con un estado: "Disponible" si AvailableCopies > 0, o "Agotado" si no hay copias disponibles.
SELECT Title,
       CASE 
           WHEN AvailableCopies > 0 THEN 'Disponible'
           ELSE 'Agotado'
       END AS Estado_Libro
FROM Books;

-- 6. Mostrar los usuarios y clasifícalos como "Activo" si tienen libros prestados y "Sin actividad" si no.
SELECT U.FirstName, U.LastName,
       CASE 
           WHEN COUNT(L.LoanID) > 0 THEN 'Activo'
           ELSE 'Sin actividad'
       END AS Estado_Usuario
FROM Users U
LEFT JOIN Loans L ON U.UserID = L.UserID
GROUP BY U.UserID, U.FirstName, U.LastName;

-- 7. Encontrar las categorías con más de 3 libros.
SELECT BC.CategoryName, COUNT(B.BookID) AS Total_Libros
FROM BookCategories BC
JOIN Books B ON BC.CategoryID = B.CategoryID
GROUP BY BC.CategoryID, BC.CategoryName
HAVING COUNT(B.BookID) > 3;

-- 8. Mostrar los usuarios que tienen más de 2 libros reservados.
SELECT U.FirstName, U.LastName, COUNT(R.ReservationID) AS Total_Reservas
FROM Users U
JOIN Reservations R ON U.UserID = R.UserID
GROUP BY U.UserID, U.FirstName, U.LastName
HAVING COUNT(R.ReservationID) > 2;

-- 9. Mostrar un listado de los nombres de usuarios y los títulos de los libros que han sido prestados.
SELECT U.FirstName, U.LastName, B.Title
FROM Users U
INNER JOIN Loans L ON U.UserID = L.UserID
INNER JOIN Books B ON L.BookID = B.BookID;

-- 10. Mostrar los nombres de usuarios y los títulos de los libros que han reservado.
SELECT U.FirstName, U.LastName, B.Title
FROM Users U
INNER JOIN Reservations R ON U.UserID = R.UserID
INNER JOIN Books B ON R.BookID = B.BookID;

-- 11. Listar todos los libros junto con el nombre del usuario que los reservó, si es que existe una reserva.
SELECT B.Title, U.FirstName, U.LastName
FROM Books B
LEFT JOIN Reservations R ON B.BookID = R.BookID
LEFT JOIN Users U ON R.UserID = U.UserID;

-- 12. Listar todos los usuarios junto con el título del libro prestado, si existe un préstamo.
SELECT U.FirstName, U.LastName, B.Title
FROM Users U
LEFT JOIN Loans L ON U.UserID = L.UserID
LEFT JOIN Books B ON L.BookID = B.BookID;

-- 13. Listar todos los libros junto con los nombres de los usuarios que los han reservado, incluyendo los libros que no tienen reservas.
SELECT B.Title, U.FirstName, U.LastName
FROM Users U
JOIN Reservations R ON U.UserID = R.UserID
RIGHT JOIN Books B ON R.BookID = B.BookID;

-- 14. Lista todos los usuarios junto con los títulos de los libros prestados, incluyendo los usuarios que no han realizado préstamos.
SELECT U.FirstName, U.LastName, B.Title
FROM Books B
JOIN Loans L ON B.BookID = L.BookID
RIGHT JOIN Users U ON L.UserID = U.UserID;

-- 15. Mostrar un listado de los títulos de los libros en mayúsculas.
SELECT UPPER(Title) AS Titulo_Mayusculas 
FROM Books;

-- 16. Mostrar los nombres de los usuarios concatenados en un solo campo (Nombre Completo).
SELECT CONCAT(FirstName, ' ', LastName) AS Nombre_Completo 
FROM Users;

-- 17. Calcular el número de días que han pasado desde que se reservó cada libro.
SELECT ReservationID, BookID, ReservationDate, 
       DATEDIFF(CURRENT_DATE, ReservationDate) AS Dias_Transcurridos
FROM Reservations;

-- 18. Mostrar los préstamos que están pendientes de devolución (ReturnDate es NULL).
SELECT LoanID, UserID, BookID, LoanDate 
FROM Loans
WHERE ReturnDate IS NULL;

-- 19. Calcular el total de copias disponibles para cada categoría.
SELECT BC.CategoryName, SUM(B.AvailableCopies) AS Copias_Totales
FROM BookCategories BC
JOIN Books B ON BC.CategoryID = B.CategoryID
GROUP BY BC.CategoryID, BC.CategoryName;

-- 20. Encontrar el número total de libros prestados por cada usuario.
SELECT U.FirstName, U.LastName, COUNT(L.LoanID) AS Libros_Prestados
FROM Users U
LEFT JOIN Loans L ON U.UserID = L.UserID
GROUP BY U.UserID, U.FirstName, U.LastName;