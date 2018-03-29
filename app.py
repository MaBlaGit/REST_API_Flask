from flask import Flask
from flask_restful import Api
from resources.user import User, UserList, UserRegister
from resources.store import Store, StoreProductList
from resources.purchase_history import PurchaseHistory
from db.database import create_database
from security import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
api = Api(app)
app.secret_key = 'test'
jwt = JWT(app, authenticate, identity)

api.add_resource(User, '/users/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/product/<string:product>')
api.add_resource(StoreProductList, '/products')
api.add_resource(PurchaseHistory, '/history/<string:name>')

if __name__ == '__main__':
    create_database('./db/datashop.db')
    app.run()
