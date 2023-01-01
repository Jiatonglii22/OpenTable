import psycopg2 as pg2

con = pg2.connect(database='socnet', user='isdb')  
con.autocommit = True
cur = con.cursor()

def get_num_reviews_for_reservations(restaurant_id : str):
	print("User Story 4")
	print("This query returns the number of the reservations at the restaurant specified by restaurant_id")
	print("and the number of the reviews made based off a reservation")
	print()
	print("For restaurant %s:"%restaurant_id)
	query1 = '''
		SELECT count(reservation_id)
		FROM Reservations
		WHERE restaurant_id = %s
	'''
	cur.execute(query1, [restaurant_id])    
	row = cur.fetchall()
	print('Number of reservations at the restaurant:', row[0][0]) 

	query2 = '''
		SELECT count(r3.review_id)
		FROM Reservations as r1 JOIN Restaurants as r2 
			ON r1.restaurant_id = r2.restaurant_id JOIN Reviews as r3
			ON r1.date = r3.dined_date AND r1.user_id = r3.user_id
		WHERE r1.restaurant_id = %s
	'''
	cur.execute(query2, [restaurant_id])    

	row = cur.fetchall()
	print('Number of reviews for reservations:', row[0][0]) 

get_num_reviews_for_reservations('REST2')