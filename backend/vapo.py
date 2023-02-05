from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    hashed_pwd = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DateTime)
    free_days = db.Column(db.Integer)
    target = db.Column(db.Integer)
    group_id = db.Column(db.Integer)

    posts = db.relationship('Post', backref='users')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False)
    num_of_members = db.Column(db.Integer)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime)
    content = db.Column(db.String(100), nullable=False)

    subposts = db.relationship('Subpost', backref='post')

class Subpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    date = db.Column(db.DateTime)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

from flask_restful import Resource
from flask import request
from flask_bcrypt import Bcrypt
import json
from datetime import datetime
from sqlalchemy import or_

class CreateUser(Resource):
    def post(self):
        # get imputs 
        data = request.data
        data = json.loads(data)
        username = data["username"]
        password = data["password"]

        # hash password
        bcrypt = Bcrypt()
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')

        # find a group or generate a group
        group = Group.query.filter(or_(Group.creation_date == datetime.today().date(), Group.num_of_members < 7)).first()
        if(not group):
            group = Group(creation_date=datetime.now(), num_of_members=0)
            db.session.add(group)
        group.num_of_members += 1 
        db.session.commit()

        user = User(username=username, hashed_pwd=hashed_pwd, date_joined=datetime.now(), free_days=0, target=7, group_id=group.id)
        db.session.add(user)
        db.session.commit()
        return 200
api.add_resource(CreateUser, '/create_user')

class Login(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)
        username = data["username"]
        password = data["password"]

        user = db.session.query(User).filter_by(username=username).first()

        if(not user):
            return {"success": False, "user_id": None}

        # hash password
        bcrypt = Bcrypt()
        match = bcrypt.check_password_hash(user.hashed_pwd, password)
        if(match):
            return {"success": True, "user_id": user.id}
        else:
            return {"success": False, "user_id": None}

api.add_resource(Login, '/login')


class GetPost(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)

        # print(data)

        user_id = data["user_id"]
        # find user first
        user = db.session.query(User).filter_by(id=user_id).first()
        # find group members
        group_members = []
        group = db.session.query(User).filter_by(group_id=user.group_id).all()
        for person in group:
            group_members.append(person)
        
        posts = []
        for person in group_members:
            curr_post = db.session.query(Post).filter_by(user_id=person.id).all()
            for post in curr_post:
                posts.append({"username": person.username, "content": post.content, "date": post.date.isoformat(), "id":post.id})
        
        return posts

api.add_resource(GetPost, '/get_post')

class GetSubPost(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)

        print(data)

        post_id = data["post_id"]
        # find user first
        post_list = db.session.query(Subpost).filter_by(post_id=post_id).all()
        
        posts = []
        for post in post_list:
            parent_post = db.session.query(Post).filter_by(id=post.post_id).first()
            user = db.session.query(User).filter_by(id=parent_post.user_id).first()
            posts.append({"username": user.username, "content": post.content, "date": post.date.isoformat()})
        
        return posts

api.add_resource(GetSubPost, '/get_sub_post')

class CreatePost(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)
        # print(data)
        user_id = data["user_id"]
        content = data["content"]

        cur_post = Post(user_id = user_id, date = datetime.now(), content = content)
        db.session.add(cur_post)
        db.session.commit()

api.add_resource(CreatePost, '/create_post')

class CreateSubPost(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)
        # print(data)
        content = data["content"]
        post_id = data["post_id"]

        cur_post = Subpost(content=content, date = datetime.now(), post_id=post_id)
        db.session.add(cur_post)
        db.session.commit()

api.add_resource(CreateSubPost, '/create_sub_post')

if __name__ == '__main__':
    app.run()