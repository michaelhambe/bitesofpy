from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class  UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
   pass

class UserNoPermission(Exception):
    pass



def get_secret_token(username):
    # users = [(n, user.name) for n, user in enumerate(USERS)]
    users = [user.name for user in USERS]
    if username in users:
        for user in USERS:
            if username == user.name:
                if user.expired == False:
                    print('valid')
                    if user.role == 'admin':
                        print('admin')
                        return SECRET
                    else:
                        raise UserNoPermission
                else:
                    raise UserAccessExpired
    else:
        raise UserDoesNotExist
        
            
# get_secret_token('Bob')

# def get_secret_token2(username):
#     try:
#         users = [user.name for user in USERS]
#         if username in users:
#             try:
#                 username_status = USERS
#                 if USERS[username].expired:
#                     pass
#                 else:
#                     raise UserAccessExpired
#             except UserAccessExpired as e:
#                 raise
                
#         else:
#             raise UserDoesNotExist("validate.UserDoesNotExist")

#     except UserDoesNotExist as e:
#         raise
