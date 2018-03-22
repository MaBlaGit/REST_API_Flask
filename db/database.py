import sqlite3

connection = sqlite3.connect('./datashop.db')
cursor = connection.cursor()

create_user_table = 'CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, username text NOT NULL, user_email text NOT NULL);'
cursor.execute(create_user_table)

create_history_table = 'CREATE TABLE IF NOT EXISTS purchase_history(id INTEGER PRIMARY KEY, product text, user_id INTEGER NOT NULL, product_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (product_id) REFERENCES store(id));'
cursor.execute(create_history_table)

create_store_table = 'CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY, product text, price FLOAT);'
cursor.execute(create_store_table)

# insertions
cursor.execute('INSERT INTO user VALUES (1, "Mariusz", "mariusz@test.pl");')
cursor.execute('INSERT INTO user VALUES (2, "Basia", "basia@test.pl");')
cursor.execute('INSERT INTO user VALUES (3, "Maurycy", "maurycy@test.pl");')
cursor.execute('INSERT INTO user VALUES (4, "Rocky", "rocky@test.pl");')
cursor.execute('INSERT INTO user VALUES (5, "Mariusz", "mariusz1@test.pl");')

cursor.execute('INSERT INTO store VALUES(1, "car", 10999.99);')
cursor.execute('INSERT INTO store VALUES(2, "bike", 45.99);')
cursor.execute('INSERT INTO store VALUES(3, "motorbike", 599.99);')
cursor.execute('INSERT INTO store VALUES(4, "go-cart", 20050.99);')

cursor.execute('INSERT INTO purchase_history VALUES(1, "car", 1, 1);')

connection.commit()
connection.close()
