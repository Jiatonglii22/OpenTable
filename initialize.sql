\c postgres
DROP DATABASE IF EXISTS socnet;

CREATE database socnet;
\c socnet

\i create.sql 

\copy Users(user_id) FROM 'users.csv' csv header; 
\copy Restaurants(restaurant_id,restaurant_name,rating,address,restaurant_phone_num) FROM 'restaurants.csv' csv header; 
\copy Tags(tag_id,tag_name) FROM 'tags.csv' csv header; 
\copy Reviews(review_id,overall_rating,food_rating,service_rating,ambience_rating,description,dined_date,user_id,restaurant_id) FROM 'reviews.csv' csv header; 
\copy Reservations(reservation_id,date,time,party_size,user_id,restaurant_id) FROM 'reservations.csv' csv header; 
\copy Public_Reservations(reservation_id) FROM 'public_reservations.csv' csv header; 
\copy Private_Reservations(reservation_id,event_type,details) FROM 'private_reservations.csv' csv header; 
\copy Menus(menu_id,restaurant_id) FROM 'menus.csv' csv header; 
\copy Guests(user_id) FROM 'guests.csv' csv header; 
\copy Food_Items(food_id,food_name,food_price,menu_id) FROM 'food_items.csv' csv header; 
\copy Customers(user_id,customer_name,customer_email,customer_phone_number) FROM 'customers.csv' csv header; 
\copy Categorized_By(restaurant_id,tag_id) FROM 'categorized_by.csv' csv header; 


-- puts new users into guests table 
CREATE OR REPLACE FUNCTION add_user_trigger_fn() 
RETURNS trigger 
LANGUAGE plpgsql AS 
$$
BEGIN 
    INSERT INTO guests 
    VALUES (new.user_id);
    return null; 

END
$$;

CREATE OR REPLACE TRIGGER user_tr AFTER INSERT ON users
FOR EACH ROW 
EXECUTE FUNCTION add_user_trigger_fn();


-- deletes from guest when guest registers as a customer 
CREATE OR REPLACE FUNCTION delete_user_trigger_fn()
RETURNS trigger 
LANGUAGE plpgsql AS 
$$
BEGIN 
    DELETE FROM guests 
     WHERE user_id = new.user_id;
    return null; 

END
$$;

CREATE OR REPLACE TRIGGER user_tr2 AFTER INSERT ON customers
FOR EACH ROW 
EXECUTE FUNCTION delete_user_trigger_fn() 
