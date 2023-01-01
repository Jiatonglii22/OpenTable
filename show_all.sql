\c postgres
\c socnet

\! echo "User ids";
SELECT * FROM Users;

\! echo "Guests ids";
SELECT * FROM Guests;

\! echo "Customer information";
SELECT * FROM Customers;

\! echo "Restaurant information";
SELECT * FROM Restaurants;

\! echo "All reservation information";
SELECT * FROM Reservations;

\! echo "Public reservation information";
SELECT * FROM Public_Reservations;

\! echo "Private reservation information";
SELECT * FROM Private_Reservations;

\! echo "Review information";
SELECT * FROM Reviews;

\! echo "Restaurant tags";
SELECT * FROM Categorized_By;

\! echo "Tag information";
SELECT * FROM Tags;

\! echo "Menu information";
SELECT * FROM Menus;

\! echo "Food item information";
SELECT * FROM Food_Items;