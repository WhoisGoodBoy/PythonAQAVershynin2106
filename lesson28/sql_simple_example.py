import psycopg2

connection = psycopg2.connect(user='postgres',
                              password='d2z76ctb',
                              host='localhost',
                              port='5432',
                              database='postgres')

cursor = connection.cursor()
cursor.execute('CREATE TABLE testtable (first_name varchar(25), age int);')
cursor.execute("INSERT INTO testtable (first_name, age) VALUES ('ordinary_name', 30),('unordinary_name', 20);")
cursor.execute('SELECT * from testtable;')
connection.commit()
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()
