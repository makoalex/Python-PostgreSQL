from psycopg2 import pool

my_connection = pool.SimpleConnectionPool(
    1, 2,
    database='Learning',
    user='postgres',
    password='karenina',
    host='localhost',
    port=5433
)
