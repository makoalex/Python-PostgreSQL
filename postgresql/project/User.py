from Database import ConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return ' User: {}.'.format(self.email)

    def save_to_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('Insert into Users (Email, First_Name, Last_name) values (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))


    @classmethod
    def load_from_db(cls, email):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('Select* from users where Email = %s', (email,))
                data = cursor.fetchone()
            print(cls(email=data[1], first_name=data[2], last_name=data[3], id=data[0]))
            return ' Email- {}\n First Name- {}\n Last Name- {}\n ID- {}'.format(data[1], data[2], data[3], data[0])
