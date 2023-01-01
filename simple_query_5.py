#User Story 9 

import psycopg2

def print_rows(rows):
    for row in rows:
        print(row)

conn = psycopg2.connect(database='socnet', user='isdb')
conn.autocommit = True
cur = conn.cursor()

def show_food_items(restaurant_id: str): 
    print("User Story 9")
    print("This query returns the food items of the restaurant specified by restaurant_id")
    print()
    print("For restaurant %s:"%restaurant_id)
    query = ''' 
        SELECT f.food_name, f.food_price 
          FROM restaurants as r 
               JOIN menus as m 
               ON r.restaurant_id = m.restaurant_id 
               JOIN food_items as f 
               ON f.menu_id = m.menu_id 
         WHERE r.restaurant_id = %s 
    '''
    cur.execute(query, [restaurant_id]) 
    rows = cur.fetchall() 
    print_rows(rows) 

show_food_items("REST3")
