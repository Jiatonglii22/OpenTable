#User Story 8 

import psycopg2  

def print_rows(rows):
    for row in rows:
        print(row)

db, user = 'socnet', 'isdb'
conn = psycopg2.connect(database=db, user=user)
conn.autocommit = True 
cur = conn.cursor()

def get_reservation_details(user_id: str): 
    print("User Story 8")
    print("This query returns the reservation details of the user specified by user_id.")
    print("Only reservations that are in the future will be shown.")
    print()
    print("Reservations for user %s:"%user_id)
    query = '''
        SELECT rv.date, rv.time, rv.party_size, r.restaurant_name, r.address
          FROM reservations as rv 
               JOIN restaurants as r 
               ON rv.restaurant_id = r.restaurant_id 
         WHERE rv.user_id = %s and rv.date > (SELECT CAST( LOCALTIMESTAMP AS Date ));
    '''
    cur.execute(query, [user_id]) 
    rows = cur.fetchall() 
    print_rows(rows)

get_reservation_details("U5")

