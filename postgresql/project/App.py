from User import User
# my_first= User('Mako@gmail.com', 'Mako', 'Chan', None)
# my_first.save_to_db()
print(User.load_from_db('Mako@gmail.com'))

