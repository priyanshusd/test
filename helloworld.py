import psycopg2
connection = psycopg2.connect(
        host="devtoppers.cagadciwq7si.us-east-1.rds.amazonaws.com",
        database="pythonapp",
        user="python",
        password="python123")

cursor = connection.cursor()
# Executing a SQL query to insert data into  table
insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
cursor.execute(insert_query)
connection.commit()
print("1 Record inserted successfully")
# Fetch result
cursor.execute("SELECT * from mobile")
record = cursor.fetchall()
print("Result ", record)

