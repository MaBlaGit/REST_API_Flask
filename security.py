from werkzeug.security import safe_str_cmp
from models.user import UserModel



def authenticate(username, password):
    user = UserModel.find_by_name(username)
    if user and safe_str_cmp(user.password, password):
        return user
    else:
        return None

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
