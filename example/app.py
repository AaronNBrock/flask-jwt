from flask import Flask
from flask_jwt import JWT, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='{}')".format(self.id)

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app)


@jwt.identity_handler
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


@jwt.authentication_handler
def authenticate(username, password, **kwargs):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


@app.route('/protected')
@jwt.jwt_required()
def protected():
    return '{}'.format(current_identity)

if __name__ == '__main__':
    app.run(host='localhost')
