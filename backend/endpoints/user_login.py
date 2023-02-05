from flask_restful import Resource
from flask import request, Blueprint
from flask_bcrypt import Bcrypt
from vapo import db, api, app
from models import User

class CreateUser(Resource):
    def get(self):
        return "I am here"
        data = request.data
        username = data["username"]
        password = data["password"]
        # hash password
        bcrypt = Bcrypt()
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, hashed_pwd=hashed_pwd)
        # db.session.add(user)
        # db.session.commit()
        return 200
api.add_resource(CreateUser, '/create_user')

class Login(Resource):
    def post(self):
        data = request.data
        username = data["username"]
        password = data["password"]

        # user = db.session.query(User).filter_by(username=username)

        # if(not user):
        #     return False

        # # hash password
        # bcrypt = Bcrypt()
        # match = bcrypt.check_password_hash(user.hashed_pwd, password)
        # return match

api.add_resource(Login, '/login')

login_bp = Blueprint('login_bp', __name__)
app.register_blueprint(login_bp)
