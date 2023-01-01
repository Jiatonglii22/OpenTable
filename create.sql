-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-12-09 19:23:10.098

-- tables
-- Table: Categorized_By
CREATE TABLE Categorized_By (
    tag_id text  NOT NULL,
    restaurant_id text  NOT NULL,
    CONSTRAINT Categorized_By_pk PRIMARY KEY (tag_id,restaurant_id)
);

-- Table: Customers
CREATE TABLE Customers (
    user_id text  NOT NULL,
    customer_name text  NOT NULL,
    customer_email text  NOT NULL,
    customer_phone_number text  NOT NULL,
    CONSTRAINT Customers_pk PRIMARY KEY (user_id)
);

-- Table: Food_Items
CREATE TABLE Food_Items (
    food_id text  NOT NULL,
    food_name text  NOT NULL,
    food_price decimal(10,2)  NOT NULL,
    menu_id text  NOT NULL,
    CONSTRAINT Food_Items_pk PRIMARY KEY (food_id)
);

-- Table: Guests
CREATE TABLE Guests (
    user_id text  NOT NULL,
    CONSTRAINT Guests_pk PRIMARY KEY (user_id)
);

-- Table: Menus
CREATE TABLE Menus (
    menu_id text  NOT NULL,
    restaurant_id text  NOT NULL,
    CONSTRAINT Menus_pk PRIMARY KEY (menu_id)
);

-- Table: Private_Reservations
CREATE TABLE Private_Reservations (
    reservation_id text  NOT NULL,
    event_type text  NOT NULL,
    details text  NOT NULL,
    CONSTRAINT Private_Reservations_pk PRIMARY KEY (reservation_id)
);

-- Table: Public_Reservations
CREATE TABLE Public_Reservations (
    reservation_id text  NOT NULL,
    CONSTRAINT Public_Reservations_pk PRIMARY KEY (reservation_id)
);

-- Table: Reservations
CREATE TABLE Reservations (
    reservation_id text  NOT NULL,
    date date  NOT NULL,
    time time  NOT NULL,
    party_size int  NOT NULL,
    restaurant_id text  NOT NULL,
    user_id text  NOT NULL,
    CONSTRAINT Reservations_pk PRIMARY KEY (reservation_id)
);

-- Table: Restaurants
CREATE TABLE Restaurants (
    restaurant_id text  NOT NULL,
    restaurant_name text  NOT NULL,
    rating decimal(2,1)  NOT NULL,
    address text  NOT NULL,
    restaurant_phone_num text  NOT NULL,
    CONSTRAINT Restaurants_pk PRIMARY KEY (restaurant_id)
);

-- Table: Reviews
CREATE TABLE Reviews (
    review_id text  NOT NULL,
    overall_rating decimal(2,1)  NOT NULL,
    food_rating decimal(2,1)  NOT NULL,
    service_rating decimal(2,1)  NOT NULL,
    ambience_rating decimal(2,1)  NOT NULL,
    description text  NOT NULL,
    dined_date date  NOT NULL,
    restaurant_id text  NOT NULL,
    user_id text  NOT NULL,
    CONSTRAINT Reviews_pk PRIMARY KEY (review_id)
);

-- Table: Tags
CREATE TABLE Tags (
    tag_id text  NOT NULL,
    tag_name text  NOT NULL,
    CONSTRAINT Tags_pk PRIMARY KEY (tag_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Categorized_By_Restaurant (table: Categorized_By)
ALTER TABLE Categorized_By ADD CONSTRAINT Categorized_By_Restaurant
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Categorized_By_Tags (table: Categorized_By)
ALTER TABLE Categorized_By ADD CONSTRAINT Categorized_By_Tags
    FOREIGN KEY (tag_id)
    REFERENCES Tags (tag_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Customer_Users (table: Customers)
ALTER TABLE Customers ADD CONSTRAINT Customer_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Food_Item_Menu (table: Food_Items)
ALTER TABLE Food_Items ADD CONSTRAINT Food_Item_Menu
    FOREIGN KEY (menu_id)
    REFERENCES Menus (menu_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Guests_Users (table: Guests)
ALTER TABLE Guests ADD CONSTRAINT Guests_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Menu_Restaurant (table: Menus)
ALTER TABLE Menus ADD CONSTRAINT Menu_Restaurant
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Private_Reservation_Reservation (table: Private_Reservations)
ALTER TABLE Private_Reservations ADD CONSTRAINT Private_Reservation_Reservation
    FOREIGN KEY (reservation_id)
    REFERENCES Reservations (reservation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Public_Reservation_Reservation (table: Public_Reservations)
ALTER TABLE Public_Reservations ADD CONSTRAINT Public_Reservation_Reservation
    FOREIGN KEY (reservation_id)
    REFERENCES Reservations (reservation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Restaurant (table: Reservations)
ALTER TABLE Reservations ADD CONSTRAINT Reservation_Restaurant
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Users (table: Reservations)
ALTER TABLE Reservations ADD CONSTRAINT Reservation_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Restaurant (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Restaurant
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Users (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.