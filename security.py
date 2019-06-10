from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username,password):
    user = UserModel.find_by_username(username)
    print('user name is ', user)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)
