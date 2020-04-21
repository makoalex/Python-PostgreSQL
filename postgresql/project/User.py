import psycopg2


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return 'User-{}.'.format(self.email)

    def save_to_db(self):
        with psycopg2.connect(database="Learning", user='postgres', password='karenina', host='localhost',
                              port=5433) as connection:
            with connection.cursor() as cursor:
                cursor.execute('Insert into Users (Email, First_Name, Last_name) values (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db(cls, email):
        with psycopg2.connect(database='Learning', user='postgres', password='karenina', host='localhost',
                              port=5433) as connection:
            with connection.cursor() as cursor:
                cursor.execute('Select* from users where Email = %s', (email,))
                data = cursor.fetchone()
                return 'Email-{},\nFirst Name-{}, \nLast Name-{}\nID-{}'.format(data[1], data[2], data[3], data[0])
