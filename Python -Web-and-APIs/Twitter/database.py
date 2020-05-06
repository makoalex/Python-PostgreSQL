from psycopg2 import pool


class Database:
    my_connection = None

    @classmethod
    def initialise_connection(cls, **kwargs):
        Database.my_connection = pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    def get_connection():
        return Database.my_connection.getconn()

    @staticmethod
    def put_back_connection(connection):
        return Database.my_connection.putconn(connection)

    @staticmethod
    def close_all_connections():
        return Database.my_connection.closeall()


class GetConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            return self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        return Database.put_back_connection(self.connection)
