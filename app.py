from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from resources.user import User, UserList, UserRegister
from resources.store import Store, StoreProductList
from db.database import create_database
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)
jwt = JWT(app, authenticate, identity)


api.add_resource(User, '/users/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/product/<string:product>')
api.add_resource(StoreProductList, '/products')

if __name__ == '__main__':
    create_database('./db/datashop.db')
    app.run()
