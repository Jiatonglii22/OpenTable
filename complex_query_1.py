
#User Story 7

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

def private_vs_public(restaurant_id): 
    print("US 7 : As a restaurant, I want to compare the amount of public to private reservations")
    print("given a restaurant id, query will return amount private reservations and public reservations made at that restaurant")
    print("Assuming that every reservation is a default public reservation if not specified as a private reservation.")
    print("for restaurant_id REST5: ")
    print("count for public reservations will be calculated first: ")
    tmpl = '''
        SELECT COUNT(r.reservation_id)
          FROM reservations as r 
               JOIN public_reservations as pub 
               ON r.reservation_id = pub.reservation_id 
         WHERE r.restaurant_id = %s
    '''
    cmd = cur.mogrify(tmpl, (restaurant_id,))
    cur.execute(cmd) 
    rows = cur.fetchall()
    print_rows(rows)

    print("count for private reservations will be calculated next: ")
    tmpl2 = '''
        SELECT COUNT(r.reservation_id)
          FROM reservations as r 
               JOIN private_reservations as pri 
               ON r.reservation_id = pri.reservation_id 
         WHERE r.restaurant_id = %s
    '''
    cmd2 = cur.mogrify(tmpl2, (restaurant_id,))
    cur.execute(cmd2)
    rows = cur.fetchall()
    print_rows(rows)

private_vs_public("REST5")