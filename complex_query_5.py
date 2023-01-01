#User Story 10 
#trigger query 

import psycopg2 

def print_rows(rows):
    for row in rows:
        print(row)

conn = psycopg2.connect(database='socnet', user='isdb')
conn.autocommit = True
cur = conn.cursor()

def update_reservation(): 
    print('User Story 10: allow another user to see your reservation details')
    show_user_table()
    # print("given the reservation_id and the user_id, function will update the party size by 1")
    user_id = input('Input your user id: ')
    rows = get_user_reservations(user_id)
    if len(rows) == 0 :
        print('No reservations found for the user. Exiting.')
        return
    reservations = []
    for row in rows:
        reservations.append(row[0])
    print(reservations)
    print('Reservations for user %s:'%user_id)
    print_rows(rows)
    reservation_id = input('Pick a reservation id from your reservations: ') 
    while reservation_id not in reservations: 
        print('Not a valid reservation id')
        reservation_id = input('Pick a reservation id from your reservations: ') 
    invite_user(user_id, reservation_id)
    update_party_size(user_id, reservation_id)


def update_party_size(user_id, reservation_id): 
    query = '''
        UPDATE Reservations
           SET party_size = party_size + 1 
         WHERE reservation_id = %s
    '''
    cur.execute(query, [reservation_id])
    print('Updated reservation:')
    row = show_individual_reservation(user_id, reservation_id)
    print('New party size:', row[2])

def show_reservation_table(): 
    query = '''
        SELECT * 
          FROM reservations
    '''
    cur.execute(query)
    rows = cur.fetchall()
    print_rows(rows)

def invite_user(user_id, reservation_id): 
    print('The selected reservation (%s):'%reservation_id)
    show_individual_reservation(user_id, reservation_id)

    usertype = input('Would you like the person you want to add to your reservation to register as a customer? (y/n): ')
    while usertype not in ('y','n'):
        print('Invalid input.')
        input('Would you like the person you want to add to your reservation to register as a customer? (y/n): ')
    if usertype == 'y':
        print('Current customer table is: ')
        show_customer_table()   
        new_user_id = generate_user_id()
        print('The generated user id for the new user is:', new_user_id)
        update_user_table(new_user_id) 
        print("Inserting into user table, which triggers an update on Guests table") 
        show_guests_table()
        customer_name = input("Give their name: ")
        customer_email = input("Give their email: ") 
        customer_phone_number = input("Give their phone number: ") 
        print("Their new information should now be part of the Customers table")
        update_customer_table(new_user_id, customer_name, customer_email, customer_phone_number) 
        show_customer_table()   
        print("They should be removed from the Guests table")
        show_guests_table()
    else:
        print("New user will be recorded as a guest")
        print("This is the current Guests table") 
        show_guests_table() 
        new_user_id = generate_user_id()
        update_user_table(new_user_id) 
        print('The generated user id for the new user is:', new_user_id)
        print("This is the updated Users table")
        show_user_table(); 
        print("Trigger updates the Guests table with new user")
        show_guests_table() 
        

def update_customer_table(new_user_id, customer_name, customer_email, customer_phone_number): 
    tmpl = '''
        INSERT INTO Customers(user_id,customer_name,customer_email,customer_phone_number)
        VALUES (%s, %s, %s, %s)
    '''
    cmd = cur.mogrify(tmpl, (new_user_id, customer_name, customer_email, customer_phone_number))
    cur.execute(cmd) 

def update_user_table(new_user_id): 
    tmpl = '''
        INSERT INTO Users(user_id)
        VALUES (%s)
    '''
    cmd = cur.mogrify(tmpl, (new_user_id,))
    cur.execute(cmd) 

def get_user_reservations(user_id): 
    tmpl = '''
        SELECT * 
          FROM Reservations
         WHERE user_id = %s
    '''
    cmd = cur.mogrify(tmpl, (user_id,))
    cur.execute(cmd)
    rows = cur.fetchall()
    return rows

def show_individual_reservation(user_id, reservation_id): 
    tmpl = '''
        SELECT res.date, res.time, res.party_size, r.restaurant_name, r.address
          FROM Reservations as res 
               JOIN Restaurants as r 
               ON res.restaurant_id = r.restaurant_id 
         WHERE user_id = %s and res.reservation_id = %s
    '''
    cmd = cur.mogrify(tmpl, (user_id, reservation_id))
    cur.execute(cmd)
    row = cur.fetchall()
    print_rows(row)
    return row[0]

def show_customer_table(): 
    tmpl = '''
        SELECT * 
          FROM Customers
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_rows(rows)

def show_user_table(): 
    tmpl = '''
        SELECT * 
          FROM Users
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_rows(rows)

def show_guests_table(): 
    tmpl = '''
        SELECT * 
          FROM Guests
    
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
        
def generate_user_id():
    query = '''
		SELECT count(user_id)
		    FROM Users
	'''

    cur.execute(query) 
    last_id = cur.fetchall()
    last_id_num = int(last_id[0][0])
    new_id = 'U' + str(last_id_num + 1)
    return new_id

update_reservation() 



