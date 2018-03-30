from models.user import UserModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class User(Resource):

    @jwt_required()
    def get(self, name):
        users = UserModel.find_by_name(name)
        if users:
            return {'user': users.json()}, 200
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

        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='This field is required!')

        data_payload = parser.parse_args()

        if UserModel.find_by_name(data_payload['username']):
            return {'message': 'User with the same name already exists in database!'}, 400
        else:
            UserModel.insert_into_table(data_payload['username'],
                                        data_payload['password'])
            return {'message': 'User successfully added to the database!'}, 201
