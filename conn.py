import psycopg2
connection = psycopg2.connect(
    database='python_Project',
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)
# cur = conn.cursor()

# if you already have any table or not id doesnt matter this
# will create a products table for you.
# cur.execute(
#     '''CREATE TABLE IF NOT EXISTS products (id serial \
#     PRIMARY KEY, name varchar(100), price float);''')

# # Insert some data into the table
# cur.execute(
#     '''INSERT INTO products (name, price) VALUES \
#     ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')

# # commit the changes
# conn.commit()

# # close the cursor and connection
# cur.close()
# conn.close()
