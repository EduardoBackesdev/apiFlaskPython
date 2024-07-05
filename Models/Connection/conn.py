import psycopg2
connection = psycopg2.connect(
    database='python_Project',
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)
