import psycopg2

connection = psycopg2.connect(user='postgres',
                              password='d2z76ctb',
                              host='localhost',
                              port='5432',
                              database='postgres')

cursor = connection.cursor()
cursor.execute('CREATE TABLE tablewithusers (id varchar(8) primary key, first_name varchar(25), last_name varchar(25), age int, email varchar(25));COMMIT;')
cursor.execute("INSERT INTO tablewithusers (id, first_name, last_name, age, email) VALUES ('AAAAAAAA','ordinary_name', 'ordinary_surname', 30, 'ordinary@gmail.com'),('BBBBBBBB','unordinary_name', 'unordinary_surname',20, 'unordinary@gmail.com'); COMMIT;")
cursor.execute('SELECT * from tablewithusers;')
connection.commit()
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()
