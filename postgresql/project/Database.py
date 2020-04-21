import psycopg2


def connect():
    return psycopg2.connect(database='Learning', user='postgres', password='karenina', host='localhost',
                            port=5433)
