from flask import Flask
from flask_restful import Api
from resources.user import User, UserList, UserRegister


app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()
