import psycopg2
connection = psycopg2.connect(
    database='project_pets',
    user='postgres',
    password='admin',
    host='localhost',
    port='5432'
)
