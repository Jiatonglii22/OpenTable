#User Story 7

import psycopg2 

conn = psycopg2.connect(database='socnet', user='isdb')
conn.autocommit = True
cur = conn.cursor()

def private_vs_public(restaurant_id: str): 
    print("User Story 7")
    print("This query returns the amount of private and public reservations made at the restaurant specified by restaurant_id.")
    print()
    print("For restaurant %s:"%restaurant_id)
    query1 = '''
        SELECT COUNT(r.reservation_id) 
          FROM reservations as r 
               JOIN public_reservations as pub 
               ON r.reservation_id = pub.reservation_id 
         WHERE r.restaurant_id = %s
    '''

    cur.execute(query1, [restaurant_id]) 
    row = cur.fetchall()
    print('Number of public reservations:', row[0][0])

    query2 = '''
        SELECT COUNT(r.reservation_id)
          FROM reservations as r 
               JOIN private_reservations as pri 
               ON r.reservation_id = pri.reservation_id 
         WHERE r.restaurant_id = %s
    '''
    cur.execute(query2, [restaurant_id]) 
    row = cur.fetchall()
    print('Number of private reservations:', row[0][0])

private_vs_public("REST2")
