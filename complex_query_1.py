import psycopg2 as pg2
from datetime import datetime

con = pg2.connect(database='socnet', user='isdb')  
con.autocommit = True
cur = con.cursor()

def create_reservation(date: str, time: str, party_size: int, user_id: str, restaurant_id: str):
    print("User Story 1")
    print("This function creates a reservation given all column values for a reservation except for the reservation_id.")
    print()

    # Create new reservation id by adding 1 to the last created id
    query = '''
		SELECT count(reservation_id)
		    FROM Reservations
	'''

    cur.execute(query) 
    last_id = cur.fetchall()
    last_id_num = int(last_id[0][0])
    new_id = 'RESV' + str(last_id_num + 1)

    print('Number of reservations before for restaurant '+ restaurant_id + ' : ', get_reservation_count(restaurant_id))
    sql_insert = '''
        INSERT INTO Reservations (reservation_id, date, time, party_size, user_id, restaurant_id) 
            VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cur.execute(sql_insert, [new_id, date, time, party_size, user_id, restaurant_id])    

    print("Created a new reservation at %s %s"%(date, time))
    print('Number of reservations after: ', get_reservation_count(restaurant_id))

def get_reservation_count(restaurant_id: str):
    query = '''
		SELECT count(reservation_id)
		    FROM Reservations
            WHERE restaurant_id = %s
	'''
    cur.execute(query, [restaurant_id])
    row = cur.fetchall()
    count = row[0][0]
    return count

create_reservation('11-20-2022', '12:00:00', 5, 'U3', 'REST4')