import psycopg2 as pg2

con = pg2.connect(database='socnet', user='isdb')  
con.autocommit = True
cur = con.cursor()

def filter_for_restaurants(tag_id : str):
	print("User Story 2")
	print("This query filters for restaurants serving cuisine specified by the tag_id")
	print()
	print("For tag %s:"%tag_id)
	query = '''
		SELECT r.restaurant_id, r.restaurant_name, t.tag_name
			FROM Restaurants as r JOIN Categorized_By as c
				ON r.restaurant_id = c.restaurant_id JOIN Tags as t
				ON c.tag_id = t.tag_id
		WHERE t.tag_id = %s
	'''
	cur.execute(query, [tag_id])    

	rows = cur.fetchall()
	for row in rows:
		print(row) 

filter_for_restaurants('TAG2')