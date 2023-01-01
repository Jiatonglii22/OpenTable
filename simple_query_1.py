#User Story 6 

import psycopg2 

def print_rows(rows):
    for row in rows:
        print(row)

db, user = 'socnet', 'isdb'
conn = psycopg2.connect(database=db, user=user)
conn.autocommit = True
cur = conn.cursor()

def show_returning_customers(restaurant_id: str): 
    print("US 6")
    print("This query returns a list of returning customers at the restaurant specified by restaurant_id")
    print("and the number of times they've made a reservation at this restaurant")
    print()
    print("For restaurant %s:"%restaurant_id)
    query = '''
        SELECT user_id, count(date)
        FROM reservations
        WHERE restaurant_id = %s
        GROUP BY user_id
        HAVING count(date) >= 2

    '''
    cur.execute(query, [restaurant_id]) 
    rows = cur.fetchall() 
    for row in rows:
        print('Customer %s has made %s reservations'%(row[0], row[1]))

show_returning_customers('REST2') 
