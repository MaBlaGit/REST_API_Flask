from models.user import UserModel
from flask_restful import Resource, reqparse


class User(Resource):

    def get(self, name):
        users = UserModel.find_by_name(name)
        if users:
            return {'user': [user.json() for user in users]}, 200
        return {'message': 'User not found!'}, 404


class UserList(Resource):

    def get(self):
        users = UserModel.find_all()
        if users:
            return {'users': [user.json() for user in users]}, 200
        return {'message': 'No users found!'}, 404

class UserRegister(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='This field is required!')

        parser.add_argument('user_email',
                            type=str,
                            required=True,
                            help='This field is required!')

        data_payload = parser.parse_args()

        UserModel.insert_into_table(data_payload['username'],
                                    data_payload['user_email'])
        return {'message': 'User successfully added to the database!'}, 201
