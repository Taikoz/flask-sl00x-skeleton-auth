from Controllers.UserController import UserController
from flask import Blueprint, request


user_route = Blueprint("user_route", __name__)


@user_route.route('/', methods=['GET'])
def get_all():
    return UserController.get_all_users()

@user_route.route('/<uuid:id>', methods=['GET'])
def get_by_id(id):
    return UserController.get_user_by_id(id)


@user_route.route('/', methods=['POST'])
def create_user():
    return UserController.create_user(request.json)



@user_route.route('/authenticate', methods=['POST'])
def authenticate_user():
    return UserController.authenticate(request.json)
