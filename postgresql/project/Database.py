from psycopg2 import pool

my_connection = pool.SimpleConnectionPool(
    1, 1,
    database='Learning',
    user='postgres',
    password='karenina',
    host='localhost',
    port=5433
)


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = my_connection.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.rollback()
        else:
            self.connection.commit()
        return my_connection.putconn(self.connection)
