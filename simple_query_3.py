import psycopg2 as pg2
from datetime import datetime

con = pg2.connect(database='socnet', user='isdb')  
con.autocommit = True
cur = con.cursor()

def get_num_bookings(restaurant_id : str, date : str):
    print("User Story 5")
    print("This query returns the number of reservations on a certain day at the restaurant specified by restaurant_id")
    print()
    print("For restaurant %s:"%restaurant_id)
    query = '''
        SELECT count(r2.reservation_id)
            FROM Restaurants as r1 JOIN Reservations as r2 
                ON r1.restaurant_id = r2.restaurant_id 
        WHERE r1.restaurant_id = %s AND r2.date = %s
    '''
    cur.execute(query, [restaurant_id, date])    

    row = cur.fetchall()
    print('Number of reservations made on %s: %s' %(date, row[0][0]))

get_num_bookings('REST2', '2022-11-26')