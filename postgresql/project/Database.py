from psycopg2 import pool

my_connection = pool.SimpleConnectionPool(
    1, 1,
    database='Learning',
    user='postgres',
    password='karenina',
    host='localhost',
    port=5433
)


class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = my_connection.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        return my_connection.putconn(self.connection)
