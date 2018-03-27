from models.store import StoreModel
from flask_restful import Resource, reqparse


class Store(Resource):

    def get(self, product):
        products = StoreModel.find_by_product(product)
        if products:
            return {'product': [product.json() for product in products]}, 200
        else:
            return{'message': 'Product not found!'}, 404

    def post(self, product):
        product = StoreModel.find_by_product(product)
        if product:
            return {'message': 'Product already in database!'}
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('product',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('price',
                                type=float,
                                required=True,
                                help='This field is mandatory!')

            data_payload = parser.parse_args()

            StoreModel.add_product(data_payload['product'],
                                    data_payload['price'])
            return {'message': 'Product successfully added to database!'}, 201

class StoreProductList(Resource):

    def get(self):
        products = StoreModel.find_all_products();
        if products:
            return {'products': [product.json() for product in products]}, 200
        else:
            return {'message': 'No products found!'}, 404
