from models.purchase_history import PurchaseHistoryModel
from flask_restful import Resource, reqparse


class PurchaseHistory(Resource):

    def get(self, name):
        list_of_products = PurchaseHistoryModel.find_products_related_with_user_name(name)
        if list_of_products:
            return {
            'product_history': [product.json() for product in list_of_products]
            }, 200
        else:
            return {
            'message': 'User and related prducts not found in database!'
            }, 404

    def post(self, name, product):
        pass
