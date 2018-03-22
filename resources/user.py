from models.user import UserModel
from flask_restful import Resource, reqparse


class User(Resource):

    def get(self, name):
        users = UserModel.find_by_name(name)
        if users:
            return {'user': [user.json() for user in users]}, 200
        return {'message': 'User not found!'}, 404

    def get(self):
        users = UserModel.find_all()
        if users:
            return {'users': [user.json() for user in users]}, 200
        return {'message': 'Users not found!'}, 404
