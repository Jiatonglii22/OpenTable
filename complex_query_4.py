
#User Story 10 
#trigger query 

import psycopg2 
import sys 

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)

db, user = 'socnet', 'isdb'
conn = psycopg2.connect(database=db, user=user)
conn.autocommit = True
cur = conn.cursor()

def update_reservation(): 
    print("US 10 : As a Customer, I want other people to see my reservation details/add other people to my reservation")
    print("given the reservation_id and the user_id, function will update the party size by 1")
    show_reservation_table()
    reservation_id = input("Input your reservation id: ") 
    user_id = input("Input your user_id: ")
    update_party_size(reservation_id)
    invite_user(user_id)

def update_party_size(reservation_id): 
    tmpl = '''
        UPDATE reservations
           SET party_size = party_size + 1 
         WHERE reservation_id = %s
    '''
    cmd = cur.mogrify(tmpl, (reservation_id,))
    cur.execute(cmd)
    show_reservation_table()

def show_reservation_table(): 
    tmpl = '''
        SELECT * 
          FROM reservations
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_rows(rows)

def invite_user(user_id): 
    print("allow an existing user to view your reservation")
    print("they will be registered as guest user")
    show_reservation_table_for_user(user_id) 
    res_id = input("select a reservation id: ")
    print("this will be the registration details sent to them") 
    show_individual_reservation(user_id, res_id)

    usertype = input("would you like the person you want to add to your reservation to register as a customer? type yes or no")
    if usertype == "yes":
        print("current customer table is: ")
        show_customer_table()   
        print("current guest table is: ")
        show_guests_table()
        new_user_id = input("give them a user_id: ")
        update_user_table(new_user_id) 
        print("should trigger an update on guests table") 
        show_guests_table()
        customer_name = input("give their name: ")
        customer_email = input("give their email: ") 
        customer_phone_number = input("give their phone number: ") 
        print("their new information should now be part of the customer's table")
        update_customer_table(new_user_id, customer_name, customer_email, customer_phone_number) 
        show_customer_table()   
        print("and they should be removed from the guests table")
        show_guests_table()
    else:
        print("new user will be recorded as a guest")
        print("this is the current user table")
        show_user_table() 
        print("this is the current guests table") 
        show_guests_table() 
        new_user_id = input("give them a user_id: ")
        update_user_table(new_user_id) 
        print("this is the updated user table")
        show_user_table(); 
        print("trigger will also update guests table with new user")
        show_guests_table() 
        

def update_customer_table(new_user_id, customer_name, customer_email, customer_phone_number): 
    tmpl = '''
        INSERT INTO customers(user_id,customer_name,customer_email,customer_phone_number)
        VALUES (%s, %s, %s, %s)
    '''
    cmd = cur.mogrify(tmpl, (new_user_id, customer_name, customer_email, customer_phone_number))
    cur.execute(cmd) 

def update_user_table(new_user_id): 
    tmpl = '''
        INSERT INTO users(user_id)
        VALUES (%s)
    '''
    cmd = cur.mogrify(tmpl, (new_user_id,))
    cur.execute(cmd) 

def show_reservation_table_for_user(user_id): 
    tmpl = '''
        SELECT * 
          FROM reservations
         WHERE user_id = %s
    '''
    cmd = cur.mogrify(tmpl, (user_id,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)

def show_individual_reservation(user_id, res_id): 
    tmpl = '''
        SELECT res.date, res.time, res.party_size, r.restaurant_name, r.address
          FROM reservations as res 
               JOIN restaurants as r 
               ON res.restaurant_id = r.restaurant_id 
         WHERE user_id = %s and r.restaurant_id = %s
    '''
    cmd = cur.mogrify(tmpl, (user_id, res_id))
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)

def show_customer_table(): 
    tmpl = '''
        SELECT * 
          FROM customers
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_rows(rows)

def show_user_table(): 
    tmpl = '''
        SELECT * 
          FROM users
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_rows(rows)

def show_guests_table(): 
    tmpl = '''
        SELECT * 
          FROM guests
    
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_rows(rows)

update_reservation() 



