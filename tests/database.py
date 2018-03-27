import sqlite3

def create_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    create_user_table = '{}{}{}'.format(
                        'CREATE TABLE IF NOT EXISTS',
                        ' user(id INTEGER PRIMARY KEY,',
                        ' username text NOT NULL, user_email text NOT NULL);'
                        )

    cursor.execute(create_user_table)

    create_history_table ='{}{}{}{}{}{}'.format(
                          'CREATE TABLE IF NOT EXISTS',
                          ' purchase_history(id INTEGER PRIMARY KEY,',
                          ' product text, user_id INTEGER NOT NULL,',
                          ' product_id INTEGER NOT NULL,',
                          ' FOREIGN KEY (user_id) REFERENCES user(id),',
                          ' FOREIGN KEY (product_id) REFERENCES store(id));'
                          )
    cursor.execute(create_history_table)

    create_store_table = '{}{}{}'.format(
                         'CREATE TABLE IF NOT EXISTS',
                         ' store(id INTEGER PRIMARY KEY,',
                         ' product text, price FLOAT);'
                         )
    cursor.execute(create_store_table)

    cursor.execute('INSERT OR REPLACE INTO user VALUES(1, "test_1", "test_1@test.pl");')
    cursor.execute('INSERT OR REPLACE INTO user VALUES(2, "test_2", "test_2@test.pl");')
    cursor.execute('INSERT OR REPLACE INTO user VALUES(3, "test_3", "test_3@test.pl");')
    cursor.execute('INSERT OR REPLACE INTO user VALUES(4, "test_4", "test_4@test.pl");')
    cursor.execute('INSERT OR REPLACE INTO user VALUES(5, "test_5", "test_5@test.pl");')

    cursor.execute('INSERT OR REPLACE INTO store VALUES(1, "car_1", 100.00);')
    cursor.execute('INSERT OR REPLACE INTO store VALUES(2, "car_2", 101.00);')
    cursor.execute('INSERT OR REPLACE INTO store VALUES(3, "car_3", 102.00);')
    cursor.execute('INSERT OR REPLACE INTO store VALUES(4, "car_4", 102.00);')

    cursor.execute('INSERT OR REPLACE INTO purchase_history VALUES(1, "car_1", 1, 1);')

    connection.commit()
    connection.close()

    print('Database successfully created and populated with data!')
