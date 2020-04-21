import psycopg2


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def save_to_db(self):
        with psycopg2.connect(database="Learning", user='postgres', password='karenina', host='localhost',
                              port=5433) as connection:
            with connection.cursor() as cursor:
                cursor.execute('Insert into Users (Email, First_Name, Last_name) values (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))
