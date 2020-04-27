from psycopg2 import pool


class Database:
    __my_connection = None

    @staticmethod
    def initialise():
        Database.__my_connection = pool.SimpleConnectionPool(
            1, 1,
            database='Learning',
            user='postgres',
            password='karenina',
            host='localhost',
            port=5433
        )

    @staticmethod
    def get_connection():
        return Database.__my_connection.getconn()

    @staticmethod
    def return_connection(connection):
        return Database.__my_connection.putconn(connection)


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        return Database.return_connection(self.connection)
