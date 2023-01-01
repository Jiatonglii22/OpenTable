
#User Story 6 

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

def show_returning_customers(restaurant_id): 
    print("US 6 : As a restaurant, I want to see my list of returning customers.")
    print("given a restaurant id, query will return a list of returning customers (customers who have made a reservation at a restaurant at least two times)")
    print("by their user_id, name, and the number of times they've made a reservation at that restaurant.")
    print("Assuming that a customer can only make a reservation once at a restaurant for that day (cannot make multiple reservations for the same restaurant on the same day).")
    print("for restaurant_id REST2, these are the returning customers: ")
    tmpl = '''
        SELECT c.user_id, c.customer_name, COUNT(r.date)
          FROM reservations as r 
               JOIN customers as c 
               ON r.user_id = c.user_id
         WHERE restaurant_id = %s 
         GROUP BY c.user_id 
        HAVING COUNT(r.date) > 1;

    '''
    cmd = cur.mogrify(tmpl, (restaurant_id,))
    cur.execute(cmd) 
    rows = cur.fetchall() 
    print_rows(rows) 

show_returning_customers("REST2") 
