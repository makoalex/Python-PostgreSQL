from User import User
user = User.load_from_db('Mako@gmail.com')
print(user)
user1 = User('new_user@yahoo.com', 'Jack', 'Don', None)
user1.save_to_db()
new = User.load_from_db('business@yahoo.com')
print(new)