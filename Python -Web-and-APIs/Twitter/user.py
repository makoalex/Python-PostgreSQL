from database import GetConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, oauth_token, oauth_token_secret, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

    def __repr__(self):
        return ' User: {}.'.format(self.email)

    def save_to_db(self):
        with GetConnectionFromPool() as cursor:
            cursor.execute('Insert into Users (email, firstname, lastname, oauth_token, oauth_token_secret) values '
                           '(%s, %s, %s, %s, %s)',
                           (self.email, self.first_name, self.last_name, self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_from_db(cls, email):
        with GetConnectionFromPool() as cursor:
            cursor.execute('Select* from users where Email = %s', (email,))
            data = cursor.fetchone()
        print(cls(email=data[1], first_name=data[2], last_name=data[3], oauth_token=data[4], oauth_token_secret=data[5],
                  id=data[0]))
        return ' Email- {}\n First Name- {}\n Last Name- {}\n Oauth Token- {}\n Oauth Token Secret {}\nID- {}'.format(
            data[1], data[2], data[3], data[4], data[5], data[0])
