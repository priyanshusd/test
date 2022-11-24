import psycopg2
connection = psycopg2.connect(
        host="devtoppers.cagadciwq7si.us-east-1.rds.amazonaws.com",
        database="pythonapp",
        user="python",
        password="python123")

cursor = connection.cursor()
create_table_query = '''CREATE TABLE mobile
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''
# Execute a command: this creates a new table
cursor.execute(create_table_query)
connection.commit()
print("Table created successfully in PostgreSQL ")
# Executing a SQL query to insert data into  table
insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
cursor.execute(insert_query)
connection.commit()
print("1 Record inserted successfully")
# Fetch result
cursor.execute("SELECT * from mobile")
record = cursor.fetchall()
print("Result ", record)

