from flask import Flask
from flask_restful import Api
from resources.user import User, UserList, UserRegister
from resources.store import Store, StoreProductList
from db.database import create_database


app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/product/<string:product>')
api.add_resource(StoreProductList, '/products')

if __name__ == '__main__':
    create_database('./db/datashop.db')
    app.run()
