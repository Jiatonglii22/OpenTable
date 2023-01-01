import psycopg2 as pg2

con = pg2.connect(database='socnet', user='isdb')  
con.autocommit = True
cur = con.cursor()

def get_reviews_by_rating(restaurant_id: str, low_rating_max : float, max_rating_min : float):
    print("User Story 3")
    print("This query returns a count of low rated reviews and high rated reviews.")
    print("The user specifies what is the maximum rating for low reviews and the minimum rating for high reviews.")
    print()
    print("For restaurant %s:"%restaurant_id)
    print('Low reviews from 0 to', low_rating_max)
    print('High reviews from', max_rating_min, 'to 5')
    query1 = '''
        SELECT count(r2.review_id)
            FROM Restaurants as r1 JOIN Reviews as r2
                ON r1.restaurant_id = r2.restaurant_id
        WHERE r1.restaurant_id = %s AND r2.overall_rating <= %s
    '''
    cur.execute(query1, [restaurant_id, low_rating_max])    

    row = cur.fetchall()
    print("Number of low reviews:", row[0][0])

    query2 = '''
        SELECT count(r2.review_id)
            FROM Restaurants as r1 JOIN Reviews as r2
                ON r1.restaurant_id = r2.restaurant_id
        WHERE r1.restaurant_id = %s AND r2.overall_rating >= %s
    '''
    cur.execute(query2, [restaurant_id, max_rating_min])    

    row = cur.fetchall()
    print("Number of high reviews:", row[0][0])


get_reviews_by_rating('REST2', 2.0, 4.0)