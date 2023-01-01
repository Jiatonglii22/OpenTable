
#User Story 8 

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

def get_reservation_details(user_id): 
    print("US 8 : As a customer, I want to see my reservation details.")
    print("given a user id, query will return their reservation details")
    print("only reservations that are in the future will be shown")
    print("for user_id U5, here are their future reservations: ") 
    tmpl = '''
        SELECT rv.date, rv.time, rv.party_size, r.restaurant_name, r.address
          FROM reservations as rv 
               JOIN restaurants as r 
               ON rv.restaurant_id = r.restaurant_id 
         WHERE rv.user_id = %s and rv.date > (SELECT CAST( LOCALTIMESTAMP AS Date ));
    '''
    cmd = cur.mogrify(tmpl, (user_id,))
    cur.execute(cmd) 
    rows = cur.fetchall() 
    print_rows(rows) 

get_reservation_details("U5")

