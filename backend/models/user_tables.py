from vapo import db

# testing db schema
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    hashed_pwd = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DateTime)
    free_days = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer)
    group_id = db.Column(db.Integer)

    posts = db.relationship('Post', backref='users')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, nullable=False)

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